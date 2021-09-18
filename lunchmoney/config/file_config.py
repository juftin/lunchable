"""
File Path Helper
"""

from pathlib import Path


class FileConfig:
    """
    Configuration Namespace for File Paths
    """

    HOME_DIR = Path.home()
    _file_config_module = Path(__file__).resolve()
    CONFIG_DIR = _file_config_module.parent
    LUNCHMONEY_DIR = CONFIG_DIR.parent
    PROJECT_DIR = LUNCHMONEY_DIR.parent
