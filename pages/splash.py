import tkinter as tk
from splashes.file_transfer import FileTransfer
from config import Config, USER_CONFIG_PATH, CRED_SECTION
import logging


class SplashPage(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.FT: FileTransfer = None
        self.disconnect_button: tk.Button = None

        self.connect_button = tk.Button(
            self, text="Connect", command=lambda: self._establish_connection()
        )
        self.connect_button.grid(row=0, column=0, padx=10, pady=10)

    def _establish_connection(self) -> None:
        if self.disconnect_button:
            self.disconnect_button.grid_forget()

        config = Config(USER_CONFIG_PATH)
        ip = config.get_config_item(CRED_SECTION, "ip")
        password = config.get_config_item(CRED_SECTION, "password")

        try:
            self.FT = FileTransfer(ip, "root", password)
        except Exception as e:
            logging.error("Failed to connect to device: %s", e)
            self._draw_info_label("Connection failed: {}".format(e), "red")
            return
        self.disconnect_button = tk.Button(
            self, text="Disconnect", command=lambda: self._disconnect_connection()
        )
        self.disconnect_button.grid(row=0, column=1, padx=(0, 10), pady=10)
        self._draw_info_label("Connected to {}".format(ip), "green")

    def _disconnect_connection(self) -> None:
        if self.FT:
            self.FT.sftp.close()
            self.FT.ssh_conn.close()
        if self.disconnect_button:
            self.disconnect_button.grid_forget()
        self.FT = None
        self.disconnect_button = None
        self._draw_info_label("Disconnected!", "yellow")

    def _draw_info_label(self, msg: str, color: str) -> None:
        row = 0
        col = 2

        info_label = self.grid_slaves(row=row, column=col)
        if info_label:
            info_label[0].grid_forget()

        info_label = tk.Label(self, text=msg, fg=color)
        info_label.grid(row=row, column=col)
