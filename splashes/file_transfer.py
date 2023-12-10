import logging
import paramiko
from splashes.splash_screens import (
    SplashScreen,
    SplashScreenPath,
    PNG_EXT,
    DEFAULT,
    REMOTE,
    BACKUP,
)


class FileTransfer:
    def __init__(self, host: str, username: str, password: str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.ssh_conn = paramiko.SSHClient()
        self.ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_conn.connect(self.host, 22, self.username, self.password)
        self.sftp = self.ssh_conn.open_sftp()

    def _put_file(self, local_path: str, remote_path: str) -> bool:
        try:
            self.sftp.put(localpath=local_path, remotepath=remote_path)
            return True
        except Exception as e:
            logging.error("Error when trying to put file on remote: %s", e)
            return False

    def _get_file(self, remote_path: str, local_path: str) -> bool:
        try:
            self.sftp.get(remotepath=remote_path, localpath=local_path)
            return True
        except Exception as e:
            logging.error("Error when trying to get file from remote: %s", e)
            return False

    def backup_splash_screen(self, splash_screen: SplashScreen) -> None:
        self._get_file(
            SplashScreenPath[splash_screen.value][REMOTE],
            SplashScreenPath[splash_screen.value][BACKUP],
        )

    def restore_splash_screen_from_backup(self, splash_screen: SplashScreen) -> None:
        self._put_file(
            SplashScreenPath[splash_screen.value][BACKUP],
            SplashScreenPath[splash_screen.value][REMOTE],
        )

    def restore_splash_screen_from_default(self, splash_screen: SplashScreen) -> None:
        self._put_file(
            SplashScreenPath[splash_screen.value][DEFAULT],
            SplashScreenPath[splash_screen.value][REMOTE],
        )

    def set_custom_splash_screen(
        self, splash_screen: SplashScreen, path_to_splash: str
    ) -> None:
        if not path_to_splash:
            raise ValueError(
                "Local file path to custom splash screen must be provided."
            )
        if path_to_splash.split(".")[-1] != PNG_EXT[1:]:
            raise ValueError("Splash screen must be a .png file.")
        self._put_file(path_to_splash, SplashScreenPath[splash_screen.value][REMOTE])
