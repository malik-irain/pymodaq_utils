from pathlib import Path
from hatchling.metadata.plugin.interface import MetadataHookInterface
import toml


class PluginInfoTomlHook(MetadataHookInterface):
    def update_custom(self, metadata: dict, here: Path) -> None:
        src_file = here.joinpath('plugin_info.toml')
        src_dict = toml.load(src_file)

        SHORT_PLUGIN_NAME: str = src_dict['plugin-info']['SHORT_PLUGIN_NAME']
        PLUGIN_NAME = f"pymodaq_plugins_{SHORT_PLUGIN_NAME}"

        metadata['authors'] = [{'name': src_dict['plugin-info']['author'],
                                'email': src_dict['plugin-info']['author-email']}]
        metadata['name'] = PLUGIN_NAME
        metadata['dependencies'] = src_dict['plugin-install']['packages-required']
        metadata['description'] = src_dict['plugin-info']['description']
        metadata['urls'] = {}
        metadata['urls']['Homepage'] = src_dict['plugin-info']['package-url']
        metadata['urls']['Documentation '] = src_dict['plugin-info']['package-url']
        metadata['urls']['Repository '] = src_dict['plugin-info']['package-url']

        entrypoints = {}
        if 'features' in src_dict:
            if src_dict['features'].get('instruments', False):
                entrypoints['pymodaq.instruments'] = {SHORT_PLUGIN_NAME: PLUGIN_NAME}
            if src_dict['features'].get('extensions', False):
                entrypoints['pymodaq.extensions'] = {SHORT_PLUGIN_NAME: PLUGIN_NAME}
            if src_dict['features'].get('pid_models', False):
                entrypoints['pymodaq.pid_models'] = {SHORT_PLUGIN_NAME: PLUGIN_NAME}
            if src_dict['features'].get('h5exporters', False):
                entrypoints['pymodaq.h5exporters'] = {SHORT_PLUGIN_NAME: PLUGIN_NAME}
            if src_dict['features'].get('scanners', False):
                entrypoints['pymodaq.scanners'] = {SHORT_PLUGIN_NAME: PLUGIN_NAME}
        else:
            entrypoints['pymodaq.instruments'] = {SHORT_PLUGIN_NAME: PLUGIN_NAME}

        entrypoints['pymodaq.plugins'] = {SHORT_PLUGIN_NAME: PLUGIN_NAME}
        # generic plugin, usefull for the plugin manager
        metadata['entry-points'] = entrypoints
