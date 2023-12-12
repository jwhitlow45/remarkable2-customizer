import tkinter as tk

# from PIL import Image, ImageTk
from splashes.file_transfer import FileTransfer
from config import Config, USER_CONFIG_PATH, CRED_SECTION
import logging


class SplashPage(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.FT: FileTransfer = None
        self.disconnect_button = tk.Button(
            self, text="Disconnect", command=lambda: self._disconnect()
        )
        self.backup_all_button = tk.Button(
            self,
            text="Backup ALL Splashes",
            command=lambda: self.FT.backup_all_splash_screens(),
        )
        self.restore_backups_button = tk.Button(
            self,
            text="Restore ALL from backups",
            command=lambda: self.FT.restore_all_splash_screens_from_backups(),
        )
        self.restore_defaults_button = tk.Button(
            self,
            text="Restore ALL from defaults",
            command=lambda: self.FT.restore_all_splash_screens_from_defaults(),
        )
        self.ui_grid: dict[tk.Button, list[int, int]] = {
            self.disconnect_button: [0, 1],
            self.backup_all_button: [1, 0],
            self.restore_backups_button: [1, 1],
            self.restore_defaults_button: [1, 2],
        }

        self.connect_button = tk.Button(
            self, text="Connect", command=lambda: self._establish_connection()
        )
        self.connect_button.grid(row=0, column=0, padx=50, pady=10)

    def _establish_connection(self) -> None:
        config = Config(USER_CONFIG_PATH)
        ip = config.get_config_item(CRED_SECTION, "ip")
        password = config.get_config_item(CRED_SECTION, "password")

        try:
            self.FT = FileTransfer(ip, "root", password)
        except Exception as e:
            logging.error("Failed to connect to device: %s", e)
            self._draw_info_label("Connection failed: {}".format(e), "red")
            return
        self._draw_page()

    def _disconnect(self) -> None:
        if self.FT:
            self.FT.sftp.close()
            self.FT.ssh_conn.close()
            self.FT = None
        self._erase_page()

    def _draw_page(self) -> None:
        self._erase_page()
        self._draw_info_label("Connected!", "green")

        for button, coords in self.ui_grid.items():
            button.grid(row=coords[0], column=coords[1], padx=(10, 0), pady=10)
        self.update_idletasks()

    def _erase_page(self) -> None:
        for button in self.ui_grid:
            button.grid_forget()
        self._draw_info_label("Disconnected!", "yellow")

    def _draw_info_label(self, msg: str, color: str) -> None:
        row = 0
        col = 2

        info_label = self.grid_slaves(row=row, column=col)
        if info_label:
            info_label[0].grid_forget()

        info_label = tk.Label(self, text=msg, fg=color)
        info_label.grid(row=row, column=col, padx=60)
