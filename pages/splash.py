import tkinter as tk
from tkinter import ttk


class SplashPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Splash Pages")
        label.grid(row=0, column=4, padx=10, pady=10)
