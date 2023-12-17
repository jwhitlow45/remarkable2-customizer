import tkinter as tk
from splashes.splash_screens import BACKUP_SPLASH_PATH, BACKUP_EXT
from pages.modules.scroller import Scroller


class BackupsPage(Scroller):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, BACKUP_SPLASH_PATH, BACKUP_EXT)
        self.no_backups_label = tk.Label(self, text="No backups found!")

    def _reload_page(self) -> None:
        super()._reload_page()
        if len(self.tk_images) == 0:
            self.no_backups_label.grid(column=self.img_x + 1, row=0)
        else:
            self.no_backups_label.grid_forget()
