import tkinter as tk
from tkinter import StringVar, ttk
from tktooltip import ToolTip
from utils.Config import get_all_options_of_section, save_config, set_config


class OptionsWindow(tk.Toplevel):
    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.title("Options")
        self.__options_dict: dict[str, dict] = {"FETCHING": {}, "LOCATIONS": {}}
        self.minsize(300, 300)
        self.__options_frame = ttk.Frame(self)
        self.__options_frame.pack(
            side="top", anchor="center", fill="x", padx=10, pady=(10, 0)
        )
        self.__options_frame.grid_columnconfigure(1, weight=1)
        self.__actions_frame = ttk.Frame(self)
        self.__actions_frame.pack(
            side="bottom", anchor="center", fill="x", padx=10, pady=(0, 10)
        )

        self.setup_options()
        self.setup_action()

    def active_button(self, *args):
        self.apply_button["state"] = "normal"

    def save_option(self):
        for section, options in self.__options_dict.items():
            for key, value in options.items():
                set_config(section, key, value.get())
        save_config()
        self.apply_button["state"] = "disabled"

    def cancel_option(self):
        self.destroy()

    def accept_option(self):
        self.save_option()
        self.cancel_option()

    def setup_action(self):
        self.cancel_button = ttk.Button(
            self.__actions_frame, text="Cancel", command=self.cancel_option
        )
        self.cancel_button.pack(side="right")
        self.apply_button = ttk.Button(
            self.__actions_frame, text="Apply", command=self.save_option
        )
        self.apply_button.pack(side="right", padx=5)
        self.apply_button["state"] = "disable"
        self.save_button = ttk.Button(
            self.__actions_frame, text="Save", command=self.accept_option
        )
        self.save_button.pack(side="right")

    def setup_options(self):
        fetching_option = get_all_options_of_section("FETCHING")
        i = 0
        for option in fetching_option:
            name, value = option
            self.__options_dict["FETCHING"][name] = StringVar(self, value=value)
            self.__options_dict["FETCHING"][name].trace_add("write", self.active_button)
            label = ttk.Label(self.__options_frame, text=name)
            label.grid(row=i, column=0, sticky="w")
            entry = ttk.Entry(
                self.__options_frame, textvariable=self.__options_dict["FETCHING"][name]
            )
            entry.grid(row=i, column=1, sticky="we")
            tip = ToolTip(entry, value, 1.0)

            i += 1
        locations_option = get_all_options_of_section("LOCATIONS")

        for option in locations_option:

            name, value = option
            self.__options_dict["LOCATIONS"][name] = StringVar(self, value=value)
            self.__options_dict["LOCATIONS"][name].trace_add(
                "write", self.active_button
            )
            label = ttk.Label(self.__options_frame, text=name)
            label.grid(row=i, column=0, sticky="w", pady=(0, 10))
            entry = ttk.Entry(
                self.__options_frame,
                textvariable=self.__options_dict["LOCATIONS"][name],
            )
            tip = ToolTip(entry, value, 1.0)
            entry.grid(row=i, column=1, sticky="we")

            i += 1
