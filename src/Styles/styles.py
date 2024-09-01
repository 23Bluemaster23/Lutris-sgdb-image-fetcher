from tkinter import Misc
from tkinter.ttk import Style


class CStyle(Style):
    def __init__(self, master: Misc | None = None) -> None:
        super().__init__(master)
        self.theme_use("clam")

        self.configure("Game.TFrame", background=self.lookup("TFrame", "background"))
        self.configure(
            "selected.Game.TFrame",
            background=self.lookup("TButton", "background", ["active"]),
        )
        self.configure(
            "pressed.Game.TFrame",
            background=self.lookup("TButton", "background", ["pressed"]),
        )
        self.configure("Game.TLabel", background=self.lookup("TFrame", "background"))
        self.configure(
            "selected.Game.TLabel",
            background=self.lookup("TButton", "background", ["active"]),
        )
        self.configure(
            "pressed.Game.TLabel",
            background=self.lookup("TButton", "background", ["pressed"]),
        )
