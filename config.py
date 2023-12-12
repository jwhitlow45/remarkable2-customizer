import os
from configparser import ConfigParser

DEFAULT_CONFIG_PATH = "." + os.path.sep + "default_config.cfg"
USER_CONFIG_PATH = "." + os.path.sep + "user_config.cfg"

CRED_SECTION = "Credentials"
FILES_SECTION = "Files"


class Config:
    def __init__(
        self, path: str = DEFAULT_CONFIG_PATH, parser: ConfigParser = None
    ) -> None:
        self.path = path
        self.parser = parser or ConfigParser()
        self.parser.read(self.path)

    def get_config_item(self, section: str, option: str) -> str:
        return self.parser.get(section, option, fallback=None)

    def save_config_item(self, section: str, option: str, value: str) -> None:
        if section not in self.parser.sections():
            self.parser.add_section(section)
        self.parser.set(section, option, value)

    def commit_config(self) -> None:
        with open(self.path, "w") as configfile:
            self.parser.write(configfile)
