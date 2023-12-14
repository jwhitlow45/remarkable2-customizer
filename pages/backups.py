import tkinter as tk
from PIL import Image, ImageTk
from splashes.splash_screens import BACKUP_SPLASH_PATH, BACKUP_EXT

from os import listdir

ASPECT_RATIO = 0.75


class BackupsPage(tk.Frame):
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.image_idx: int = 0

        # images
        self.tk_images: list[ImageTk.PhotoImage] = []
        self.label_images: list[tk.Label] = []
        self.label_names: list[tk.Label] = []

        # image dimensions
        self.img_height: int = 350
        self.img_width: int = int(self.img_height * ASPECT_RATIO)

        # label placement
        self.label_x: int = 0
        self.label_y: int = 0
        self.label_padding: int = 10
        self.label_colspan: int = 3

        # image placement
        self.img_x: int = 0
        self.img_y: int = 1
        self.img_x_pad: int = 20
        self.img_y_pad: int = 0
        self.img_colspan: int = 3

        # buttons
        self.btn_y = 2

        self.__import_backup_images()
        self._draw_image_with_label()
        self.__draw_navigation_buttons()

    def _draw_image_with_label(self) -> None:
        self.label_names[self.image_idx].grid(
            column=self.label_x,
            row=self.label_y,
            padx=self.label_padding,
            pady=self.label_padding,
            columnspan=self.label_colspan,
        )
        self.label_images[self.image_idx].grid(
            column=self.img_x,
            row=self.img_y,
            padx=self.img_x_pad,
            pady=self.img_y_pad,
            columnspan=self.img_colspan,
        )

    def _clear_image_with_label(self) -> None:
        self.label_names[self.image_idx].grid_forget()
        self.label_images[self.image_idx].grid_forget()

    def _navigate(self, amount: int) -> None:
        new_img_idx = self.image_idx + amount
        if new_img_idx < 0 or new_img_idx >= len(self.label_images):
            return

        self._clear_image_with_label()
        self.image_idx = new_img_idx
        self.img_count_label.config(
            text=f"{self.image_idx + 1}/{len(self.label_images)}"
        )
        self._draw_image_with_label()
        self.update_idletasks()

    def __import_backup_images(self):
        for file in listdir(BACKUP_SPLASH_PATH):
            if file.endswith(BACKUP_EXT):
                raw_image = Image.open(BACKUP_SPLASH_PATH + file).resize(
                    (self.img_width, self.img_height)
                )
                self.tk_images.append(ImageTk.PhotoImage(raw_image))
                raw_image.close()
                img_label = tk.Label(self)
                img_label.configure(image=self.tk_images[-1])
                self.label_images.append(img_label)
                self.label_names.append(tk.Label(self, text=file))

    def __draw_navigation_buttons(self) -> None:
        self.img_count_label = tk.Label(
            self, text=f"{self.image_idx + 1}/{len(self.label_images)}"
        )
        self.img_count_label.grid(column=self.img_x + 1, row=self.img_y + 1)
        self.left_button = tk.Button(self, text="<", command=lambda: self._navigate(-1))
        self.left_button.grid(column=self.img_x, row=self.btn_y)
        self.right_button = tk.Button(self, text=">", command=lambda: self._navigate(1))
        self.right_button.grid(column=self.img_x + 2, row=self.btn_y)
