from struct import Struct
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageOps
from interface.Components import ImageFrame
from interface.SearchWindow import SearchDialog
from utils.Config import get_filename
from utils.FileUtils import is_file


class DetailWindow(tk.Toplevel):
    def __init__(
        self,
        master: tk.Misc | None = None,
        game: Struct = None,
    ) -> None:
        super().__init__(master)
        self.title("Detalles")
        self.minsize(600, 500)
        self.game = game
        self.setup_window()

    def setup_window(self):
        self.images_frame = ttk.Frame(self)
        self.images_frame.pack(side="top", anchor="center", padx=10, pady=10)

        self.details_frame = ttk.Frame(self)
        self.details_frame.pack(side="top", anchor="center", padx=10, pady=10)

        self.coverart_path = get_filename("coverart", self.game.slug)
        self.coverart_file = ImageOps.contain(
            Image.open(
                self.coverart_path
                if is_file(self.coverart_path)
                else "src/assets/default.png"
            ),
            (120, 160),
        )

        self.coverart_img = ImageTk.PhotoImage(self.coverart_file)
        self.coverart_frame = ImageFrame(self.images_frame, self.coverart_img)
        self.coverart_frame.pack(side="left", anchor="center")

        self.banner_path = get_filename("banner", self.game.slug)

        self.banner_file = ImageOps.contain(
            Image.open(
                self.banner_path
                if is_file(self.banner_path)
                else "src/assets/default.png"
            ),
            (184, 69),
        )

        self.banner_img = ImageTk.PhotoImage(self.banner_file)
        self.banner_frame = ImageFrame(self.images_frame, self.banner_img)
        self.banner_frame.pack(side="left", anchor="center", padx=10)

        self.icon_path = get_filename("icon", self.game.slug)

        self.icon_file = ImageOps.contain(
            Image.open(
                self.icon_path if is_file(self.icon_path) else "src/assets/default.png"
            ),
            (184, 69),
        )

        self.icon_img = ImageTk.PhotoImage(self.icon_file)
        self.icon_frame = ImageFrame(self.images_frame, self.icon_img)
        self.icon_frame.pack(side="left", anchor="center")
        self.name_label = ttk.Label(self.details_frame, text=self.game.name)
        self.name_label.pack(side="top", anchor="center")
        self.platform_label = ttk.Label(self.details_frame, text=self.game.platform)
        self.platform_label.pack(side="top", anchor="center")
        self.search_button = ttk.Button(
            self, text="Search", style="TButton", command=self.show_search_dialog
        )
        self.search_button.pack(side="top", anchor="center")

    def show_search_dialog(self):
        dialog = SearchDialog(self, name=self.game.name, slug=self.game.slug)
        dialog.wm_attributes("-type", "normal")
        dialog.transient(self)
        dialog.wait_visibility()
        dialog.grab_set()
