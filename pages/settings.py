import tkinter as tk
from config import Config, USER_CONFIG_PATH, CRED_SECTION
from socket import inet_aton
import logging

IP = "ip"
PASSWORD = "password"
DEFAULT_IP = "0.0.0.0"
DEFAULT_PASSWORD = "password"


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)

        self.config = Config(USER_CONFIG_PATH)

        ip_str_value = self.config.get_config_item(CRED_SECTION, IP) or DEFAULT_IP
        password_str_value = (
            self.config.get_config_item(CRED_SECTION, PASSWORD) or DEFAULT_PASSWORD
        )
        self.ip_str = tk.StringVar(value=ip_str_value)
        self.pass_str = tk.StringVar(value=password_str_value)

        vcmd = (self.register(self._valid_ip_chars), "%P")
        ip_label = tk.Label(self, text="IP Address:")
        ip_label.grid(row=0, column=0, padx=10, pady=20)
        ip_input = tk.Entry(
            self,
            textvariable=self.ip_str,
            validate="all",
            validatecommand=vcmd,
            justify="center",
        )
        ip_input.grid(row=0, column=1)

        password_label = tk.Label(self, text="Password:")
        password_label.grid(row=1, column=0, padx=10)
        password_input = tk.Entry(self, textvariable=self.pass_str, justify="center")
        password_input.grid(row=1, column=1, padx=10)

        save_button = tk.Button(
            self, text="Save", command=lambda: self._save_settings()
        )
        save_button.grid(row=2, column=1, pady=10)

    def _valid_ip_chars(self, input: str) -> bool:
        if input == "":
            return True
        if len(input) > 15:
            return False
        if input[-1] in "0123456789.":
            return True

        return False

    def _is_valid_ip(self) -> bool:
        try:
            inet_aton(self.ip_str.get())
        except Exception as _:
            return False
        return True

    def _draw_info_label(self, msg: str, color: str) -> None:
        row = 3
        col = 1

        info_label = self.grid_slaves(row=row, column=col)
        if info_label:
            info_label[0].grid_forget()

        info_label = tk.Label(self, text=msg, fg=color)
        info_label.grid(row=row, column=col)

    def _save_settings(self):
        error = ""

        if not self._is_valid_ip():
            error = "IP address is invalid!"
        elif not self.pass_str.get().strip():
            error = "Password cannot be empty!"

        if error:
            self._draw_info_label(error, "red")
            logging.info("Failed to save...%s", error.lower())
        else:
            self.config.save_config_item(CRED_SECTION, IP, self.ip_str.get())
            self.config.save_config_item(CRED_SECTION, PASSWORD, self.pass_str.get())
            self.config.commit_config()
            self._draw_info_label("Saved!", "green")
            logging.info("Saved user credentials.")
