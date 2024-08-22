import importlib.util
import os
import sys
from pathlib import Path

import warnings

try:
    # with open(str(Path(__file__).parent.joinpath('resources/VERSION')), 'r') as fvers:
    #     __version__ = fvers.read().strip()

    from pymodaq_utils.logger import set_logger
    from pymodaq_utils.utils import get_version, PackageNotFoundError
    try:
        __version__ = get_version('pymodaq_utils')
    except PackageNotFoundError:
        __version__ = '0.0.0dev'
    try:
        LOGGER = set_logger('pymodaq', add_handler=True, base_logger=True)
    except Exception:
        print("Couldn't create the local folder to store logs , presets...")

    LOGGER.info('')
    LOGGER.info('')

    from pymodaq_utils.config import Config

    CONFIG = Config()  # to ckeck for config file existence, otherwise create one


except Exception as e:
    try:
        LOGGER.exception(str(e))
    except Exception as e:
        print(str(e))
