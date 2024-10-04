import tkinter as tk
import threading
from tkinter import ttk
from tkinter import dialog
from tkinter.simpledialog import SimpleDialog
from utils.Config import get_filename
from utils.FileUtils import dict_to_struct
from utils.SGDBAPI import (
    get_game_banner,
    get_game_coverart,
    get_game_icon,
    get_games_search,
)
from utils.WebImage import WebImage
from .Components import GameFrame, ImageFrame, ScrollFrame


class SearchDialog(tk.Toplevel):
    def __init__(
        self,
        master: tk.Misc | None = None,
        name: str = "",
        slug: str = "",
        **Kwargs,
    ) -> None:
        super().__init__(master, **Kwargs)
        self.name: str = name
        self.slug: str = slug
        self.images: dict[str, WebImage] = {
            "coverart": None,
            "banner": None,
            "icon": None,
        }

        self.minsize(500, 400)
        self.title("Search Game")
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(side="top", anchor="nw", fill="x")

        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.insert(0, self.name)
        self.search_entry.pack(
            side="left", anchor="w", fill="x", expand=True, padx=(0, 10), ipady=1
        )

        self.search_button = ttk.Button(
            self.search_frame, text="Search", style="TButton", command=self.search_game
        )
        self.search_button.pack(side="top", anchor="e")

        self.games_frames = ScrollFrame(self)

        self.games_frames._parent_frame.pack(
            side="top", anchor="nw", fill="both", expand=True
        )

    def search_game(self):
        self.games_frames.clear_frame()
        self.name = self.search_entry.get()
        res = get_games_search(self.name)
        if res != None:
            for game in res:
                sgame = dict_to_struct(game)
                game_frame = GameFrame(self.games_frames, game=sgame)
                game_frame.bind_on_frame(self.start_change_dialog, id=sgame.id)
                game_frame.pack(side="top", anchor="w", fill="x")

    def start_change_dialog(self, id):
        dialog = ImageDialog(self, id, mode="coverart", changeEvt=self.on_select_images)
        dialog.wm_attributes("-type", "normal")
        dialog.transient(self)
        dialog.wait_visibility()
        dialog.grab_set()
        thread = threading.Thread(target=dialog.setup_images)
        thread.start()

    def on_select_images(self, images: dict):
        self.images = images

        for key, image in self.images.items():
            if image != None:
                image.save_image(type=key, file_name=get_filename(key, self.slug))


class ImageDialog(tk.Toplevel):
    def __init__(
        self,
        master: tk.Misc | None = None,
        id: int = 0,
        mode: str = "coverart",
        changeEvt=None,
    ) -> None:
        super().__init__(
            master,
        )
        self.dialog = ttk.Frame(self)
        self.dialog_label = ttk.Label(self.dialog, text="Loading")
        self.images = {"coverart": "", "banner": "", "icon": ""}
        self.change_evt = changeEvt
        self.mode = mode
        self.game_id = id
        self.image_frame = tk.Text(
            self,
            wrap="char",
            borderwidth=0,
            highlightthickness=0,
            state="disabled",
            cursor="arrow",
        )
        self.image_frame.tag_configure("center", justify="center")

        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.image_frame.yview
        )
        self.image_frame.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", anchor="ne", fill="y", expand=False)
        self.image_frame.pack(
            side="left", anchor="center", fill="both", expand=True, padx=10
        )

        self.dialog.place(
            x=10,
            y=10,
        )
        self.dialog.lift(self.image_frame)

    def setup_images(self):
        self.dialog_label.pack()
        self.dialog.lift(self.image_frame)
        self.dialog.update()
        for key, value in self.images.items():

            if value == "":
                self.title("Fetching " + key.capitalize())
                res = self.get_game_image(key)
                self.set_game_image(res, key)
                self.dialog_label.pack_forget()
                self.dialog.lower()
                break

        if not "" in self.images.values():
            self.change_evt(self.images)
            self.destroy()

    def on_frame_click(self, image, type):
        self.images[type] = image
        self.clear_frame()
        self.setup_images()

    def get_game_image(self, mode: str):
        match (mode):
            case "coverart":
                return get_game_coverart(self.game_id)
            case "banner":
                return get_game_banner(self.game_id)
            case "icon":
                return get_game_icon(self.game_id)
            case _:
                return get_game_coverart(self.game_id)

    def set_game_image(self, res, type):
        image_list = []
        if len(res) > 0:
            for banner in res:
                sbanner = dict_to_struct(banner)
                image = WebImage(sbanner.url)
                frame = ImageFrame(self.image_frame, image.get_image())
                frame.bind_on_frame(self.on_frame_click, image=image, type=type)
                image_list.append(frame)

            for image in image_list:
                self.image_frame.window_create(
                    "end", window=image, align="center", stretch=True, padx=10, pady=5
                )
                self.image_frame.tag_add("center", "1.0", "end")
        else:
            self.images[type] = None

    def clear_frame(self):

        for frame in self.image_frame.winfo_children():
            frame.destroy()

        self.update()
