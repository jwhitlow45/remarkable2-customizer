import tkinter as tk
from pages.settings import SettingsPage, DEFAULT_IP
from pages.splash import SplashPage
from static_deps.TkinterSidebar2 import Sidebar
from config import Config, USER_CONFIG_PATH, CRED_SECTION

from icons.path import ICON_PATH

PAGES = (SplashPage, SettingsPage)


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Remarkable2 Customizer")
        self.geometry("810x400")

        sidebar = Sidebar(self)
        sidebar.add_spacer("Navigation")
        sidebar.add_button(
            "Splash Pages",
            lambda: self.show_frame(SplashPage),
            icon=ICON_PATH + "settings.png",
        )
        sidebar.add_button(
            "Settings",
            lambda: self.show_frame(SettingsPage),
            icon=ICON_PATH + "settings.png",
        )

        container = tk.Frame(self)
        container.pack(side="left", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)

        self.frames = {}

        # init all pages
        for F in PAGES:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=400, column=400, sticky="nsew")

        if Config(USER_CONFIG_PATH).get_config_item(CRED_SECTION, "ip") == DEFAULT_IP:
            self.show_frame(PAGES[1])
        else:
            self.show_frame(PAGES[0])

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = TkinterApp()
app.mainloop()
