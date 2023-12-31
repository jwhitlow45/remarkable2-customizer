from enum import Enum
from config import Config
import os
from config import FILES_SECTION


CONFIG = Config()

DEFAULT = "default"
REMOTE = "remote"
BACKUP = "backup"

REMOTE_SPLASH_PATH = CONFIG.get_config_item("Files", "remotesplashscreenpath")
DEFAULT_SPLASH_PATH = (
    os.path.join(
        *CONFIG.get_config_item("Files", "defaultsplashscreenpath")
        .replace("\\", " ")
        .replace("/", " ")
        .split()
    )
    + os.path.sep
)
BACKUP_SPLASH_PATH = (
    os.path.join(
        *CONFIG.get_config_item("Files", "backupsplashscreenpath")
        .replace("\\", " ")
        .replace("/", " ")
        .split()
    )
    + os.path.sep
)
BACKUP_EXT = ".bak"
PNG_EXT = ".png"
TMP_EXT = ".tmp"


class SplashScreen(Enum):
    BATTERYEMPTY = "BATTERYEMPTY"
    OVERHEATING = "OVERHEATING"
    POWEROFF = "POWEROFF"
    REBOOTING = "REBOOTING"
    RESTART = "RESTART"
    STARTING = "STARTING"
    SUSPENDED = "SUSPENDED"


SplashScreenPath = {}

for splash in SplashScreen:
    SplashScreenPath[splash.value] = {
        DEFAULT: DEFAULT_SPLASH_PATH
        + CONFIG.get_config_item(FILES_SECTION, splash.value.lower()),
        REMOTE: REMOTE_SPLASH_PATH
        + CONFIG.get_config_item(FILES_SECTION, splash.value.lower()),
        BACKUP: BACKUP_SPLASH_PATH
        + CONFIG.get_config_item(FILES_SECTION, splash.value.lower())
        + BACKUP_EXT,
    }
