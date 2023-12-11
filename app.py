import tkinter as tk
from pages.settings import SettingsPage
from pages.home import HomePage
from static_deps.TkinterSidebar2 import Sidebar

from icons.path import ICON_PATH

PAGES = (SettingsPage, HomePage)


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Remarkable2 Customizer")
        self.geometry("800x400")

        sidebar = Sidebar(self)
        sidebar.add_spacer("Splash Screens")
        sidebar.add_button(
            "Home", lambda: self.show_frame(HomePage), icon=ICON_PATH + "settings.png"
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

        self.show_frame(PAGES[0])

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = TkinterApp()
app.mainloop()
