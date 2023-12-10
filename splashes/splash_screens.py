from enum import Enum
from config import Config
import os


CONFIG = Config()
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
FILES = "Files"


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
        "default": DEFAULT_SPLASH_PATH
        + CONFIG.get_config_item(FILES, splash.value.lower()),
        "remote": REMOTE_SPLASH_PATH
        + CONFIG.get_config_item(FILES, splash.value.lower()),
        "backup": BACKUP_SPLASH_PATH
        + CONFIG.get_config_item(FILES, splash.value.lower())
        + BACKUP_EXT,
    }
