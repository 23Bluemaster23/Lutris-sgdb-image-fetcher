import tkinter as tk
from Styles import styles

from database.Manager import DbManager
from interface.DetailWindow import DetailWindow
from utils.Config import get_config
from utils.FileUtils import dict_to_struct

from .Components import AppMenu, GameFrame, ScrollFrame


class MainWindow(tk.Tk):
    def __init__(
        self,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.style = styles.CStyle()
        self.minsize(500, 400)
        self.title("Lutris STGDB Fetcher")
        self.__db_manager = DbManager(db=get_config("LOCATIONS", "db"))
        self.__games_frame = ScrollFrame(self)
        self.__games_frame._parent_frame.pack(
            side="top", anchor="nw", fill="both", expand=True
        )
        self.app_menu = AppMenu(self)
        self.config(menu=self.app_menu)
        self.update_game_list()

    def update_game_list(self):
        games = self.__db_manager.get_table_data(
            "games", ("id", "name", "slug", "platform")
        )

        for game in games:

            game_frame = GameFrame(self.__games_frame, dict_to_struct(dict(game)))
            game_frame.bind_on_frame(self.show_detail_window, game=game_frame.game)
            game_frame.pack(side="top", anchor="w", fill="x")

    def show_detail_window(self, game):
        window = DetailWindow(self, game=game)
        window.wm_attributes("-type", "normal")
        window.transient(self)
        window.wait_visibility()
        window.grab_set()
