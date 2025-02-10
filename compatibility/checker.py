import chardet
import logging
import ast
import sys
from pathlib import Path
import subprocess
import importlib


from pymodaq_plugin_manager.utils import get_pymodaq_version
from pymodaq_plugin_manager.validate import get_plugins, get_pypi_pymodaq, get_package_metadata, get_pypi_plugins

REPORT_FOLDER = Path("./reports/")

def _detect_encoding(filename):
    with open(filename, "rb") as f:
        raw = f.read()
        return chardet.detect(raw)['encoding']

class PyMoDAQPlugin:
    def __init__(self, name, version):
        self._name = name
        self._version = version
        self._install_result = None

    @property
    def name(self):
        return self._name
    
    @property
    def version(self):
        return self._version
    
    def _get_location(self):
        return importlib.util.find_spec(self._name).submodule_search_locations[0]

    def install(self) -> bool:
        #print(f'Trying to install {self._name}=={self._version}')
        command = [sys.executable, '-m', 'pip', 'install', f'{self._name}=={self._version}']
        self._install_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return self._install_result.returncode == 0

    def _save_report(self, name, stream):
        with open(REPORT_FOLDER / name, 'w') as f:
            f.write(stream)

    def save_install_report(self):
        self._save_report(f'install_report_{self._name}_{self._version}.txt', self._install_result.stdout)
    
    def save_import_report(self):
        self._save_report(f'import_report_{self._name}_{self._version}.txt', '\n'.join(self._failed_imports + [''])) 

    def all_imports_valid(self) -> bool:
        self._failed_imports = []
        install_path = self._get_location()

        for filename in Path(install_path).glob('**/*.py'):
            with open(filename, 'r', encoding=_detect_encoding(filename)) as f:
                tree = ast.parse(f.read(), filename=filename)
                for node in tree.body:
                    try:
                        if (isinstance(node, ast.ImportFrom) and 'pymodaq' in node.module) \
                        or (isinstance(node, ast.Import) and any('pymodaq' in name.name for name in node.names)):
                            for name in node.names:
                                try:
                                    if isinstance(node, ast.ImportFrom):
                                        import_code = f'from {node.module} import {name.name}'
                                        getattr(importlib.import_module(node.module), name.name)                            
                                    elif isinstance(node, ast.Import):
                                        import_code = f'import {name.name}'
                                        if name.asname:
                                            import_code += f' as {name.asname}'
                                        importlib.import_module(node.module)
                                
                                except (ImportError, ModuleNotFoundError):
                                    self._failed_imports.append(f'"{import_code}" in {filename} ({node.lineno})') 
                                except Exception as e:
                                    print(f'Unknown: {e}')
                    except TypeError as te:
                        pass
        
        return len(self._failed_imports) == 0



def main():
    code = 0
    REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

    plugin_list = get_pypi_plugins()
    
    for p in plugin_list:
        plugin = PyMoDAQPlugin(p['plugin-name'], p['version'])
        if plugin.install():
            if not plugin.all_imports_valid():
                plugin.save_import_report()
                code = 1
        else:
            plugin.save_install_report()
            code = 1
    sys.exit(code)
if __name__ == '__main__':
    main()
