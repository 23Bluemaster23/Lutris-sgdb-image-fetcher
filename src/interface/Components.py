import tkinter.ttk as ttk
import tkinter as tk
from tkinter.font import Font

from interface.OptionsWindow import OptionsWindow


class ScrollFrame(ttk.Frame):
    def __init__(
        self,
        master: tk.Misc | None = None,
        style: str = "",
    ) -> None:
        self.master = master
        self._parent_frame = ttk.Frame(master=master)
        self._parent_canvas = tk.Canvas(self._parent_frame)
        super().__init__(self._parent_canvas)
        self._scrollbar = ttk.Scrollbar(
            self._parent_frame, orient="vertical", command=self._parent_canvas.yview
        )
        self.bind("<Configure>", self.onFrameConfigure)
        self._parent_canvas.bind("<Configure>", self.onCanvasConfigure)

        self.frame_id = self._parent_canvas.create_window(
            0, 0, window=self, anchor="nw", tags=("canvas_frame",)
        )
        self._parent_canvas.configure(yscrollcommand=self._scrollbar.set)

        self._parent_canvas.pack(side="left", anchor="w", fill="both", expand=True)
        self._scrollbar.pack(side="right", fill="y")

    def onFrameConfigure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self._parent_canvas.configure(
            scrollregion=self._parent_canvas.bbox("all"), height=event.height
        )

    def onCanvasConfigure(self, event):
        """Reset the canvas window to encompass inner frame when required"""
        canvas_width = event.width
        canvas_frame: ttk.Frame = self._parent_canvas.nametowidget(
            self._parent_canvas.itemcget("canvas_frame", "window")
        )
        self._parent_canvas.itemconfigure(self.frame_id, width=canvas_width)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()


class GameFrame(ttk.Frame):
    def __init__(
        self,
        master: tk.Misc | None = None,
        game: dict = None,
    ) -> None:
        super().__init__(master, cursor="hand2", style="Game.TFrame")
        self.configure(borderwidth=1, relief="solid")

        self.game = game
        self.bind("<Enter>", lambda e: self.set_frame_status("enter"))
        self.bind("<Leave>", lambda e: self.set_frame_status("leave"))
        self.bind("<Button-1>", lambda e: self.set_frame_status("pressed"), add=["+"])
        self.bind("<ButtonRelease-1>", lambda e: self.set_frame_status("leave"))
        self.game_id = self.game.id

        self.name_label = ttk.Label(
            self, text=self.game.name, style="Game.TLabel", class_="SuperLabel"
        )
        self.name_label.bind("<Button-1>", lambda e: self.set_frame_status("pressed"))
        self.name_label.bind(
            "<ButtonRelease-1>", lambda e: self.set_frame_status("leave")
        )
        self.name_label.pack(side="top", anchor="w", pady=(4, 2))
        self.platform_label = ttk.Label(self, font=Font(size=8))
        self.platform_label.bind(
            "<Button-1>", lambda e: self.set_frame_status("pressed")
        )
        self.platform_label.bind(
            "<ButtonRelease-1>", lambda e: self.set_frame_status("leave")
        )
        if hasattr(self.game, "platform"):
            self.platform_label.configure(text=self.game.platform)
            self.platform_label.pack(side="top", anchor="w", pady=(2, 4))

    def set_frame_status(self, status: str):
        # print(status)
        match (status):
            case "enter":
                self.configure(style="selected.Game.TFrame")
                self.name_label.configure(style="selected.Game.TLabel")
                self.platform_label.configure(style="selected.Game.TLabel")
            case "pressed":
                self.configure(style="pressed.Game.TFrame")
                self.name_label.configure(style="pressed.Game.TLabel")
                self.platform_label.configure(style="pressed.Game.TLabel")
            case _:
                self.configure(style="Game.TFrame")
                self.name_label.configure(style="Game.TLabel")
                self.platform_label.configure(style="Game.TLabel")

    # def bind_on_frame(self, event):
    #     self.bind("<Button-1>", lambda e: event(self.game))
    #     self.name_label.bind("<Button-1>", lambda e: event(self.game))
    #     self.platform_label.bind("<Button-1>", lambda e: event(self.game))

    def bind_on_frame(self, event, **args):
        self.bind("<Button-1>", lambda e: event(**args))
        self.name_label.bind("<Button-1>", lambda e: event(**args))
        self.platform_label.bind("<Button-1>", lambda e: event(**args))


class ImageFrame(ttk.Frame):
    def __init__(
        self, master: tk.Misc | None = None, image: tk.PhotoImage = None, **kwargs
    ) -> None:
        super().__init__(master, borderwidth=2, relief="solid", **kwargs)
        self.image = image

        self.label = ttk.Label(self, image=self.image)
        self.label.image = self.image
        self.label.pack(side="top", anchor="center", fill="both", padx=5, pady=5)

    def bind_on_frame(self, event, **args):
        self.bind("<Button-1>", lambda e: event(**args))
        self.label.bind("<Button-1>", lambda e: event(**args))


class AppMenu(tk.Menu):
    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master

        self.tools_menu = tk.Menu(self)
        self.add_cascade(menu=self.tools_menu, label="Tools")
        self.tools_menu.add_command(label="Options", command=self.show_options_menu)

    def show_options_menu(self):
        window = OptionsWindow(master=self.master)
        window.wm_attributes("-type", "normal")
        window.transient(self.master)
        window.wait_visibility()
        window.grab_set()
