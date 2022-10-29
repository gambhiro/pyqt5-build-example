import os
from pathlib import Path
from typing import Optional
import appdirs
import platform

IS_LINUX = (platform.system() == 'Linux')
IS_WINDOWS = (platform.system() == 'Windows')
IS_MAC = (platform.system() == 'Darwin')

SMALLAPP_PACKAGE_DIR = Path(os.path.dirname(__file__)).absolute()

PACKAGE_ASSETS_DIR = SMALLAPP_PACKAGE_DIR.joinpath('assets')

SMALLAPP_DIR = Path(appdirs.user_data_dir('smallapp'))

SMALLAPP_LOG_PATH = SMALLAPP_DIR.joinpath('log.txt')

def create_app_dirs():
    if not SMALLAPP_DIR.exists():
        SMALLAPP_DIR.mkdir(parents=True, exist_ok=True)

class AppData:
    api_url: Optional[str] = None

    def __init__(self, api_port: Optional[int] = None):
        self.api_url: Optional[str] = None

        if api_port:
            self.api_url = f'http://localhost:{api_port}'
