import gi
gi.require_version("Gtk","3.0")

from gi.repository import Gtk

from controllers.SQLiteGames import SQLiteGamesController
from .GameData import GameData
from .SettingWindows import SettingWindow

class MainWindow(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_from_file("templates/MainWindow.glade")
        self.main_window = self.get_object('MainWindow')
        self.handlers = {
            'onDestroy':Gtk.main_quit,
            'on_settings_item_activate':self.open_settings
        }
        self.connect_signals(self.handlers)
        self.game_list = self.get_object('game_list')
        
        self.setup_game_list()
        
        self.main_window.show_all()
        
    def setup_game_list(self):
        res = SQLiteGamesController.get_games()
        
        for item in res:
            row = GameRow(item).game_row
            self.game_list.pack_start(row,0,1,0)
    def open_settings(self,widget):
        settings_w = SettingWindow()
class GameRow(Gtk.Builder):
    def __init__(self,game_data):
        super().__init__()
        self.game_data = game_data
        self.add_from_file('templates/GameRow.glade')
        self.game_row = self.get_object('game_row')
        self.get_object('GameRow').remove(self.game_row)
        handlers = {
            'on_edit_button_clicked':self.show_game_data,
        }
        self.connect_signals(handlers)
        self.name_label :Gtk.Label= self.get_object('name_label')
        self.platform_label :Gtk.Label = self.get_object('platform_label')
        self.slug_label :Gtk.Label = self.get_object('slug_label')
        
        self.name_label.set_text(game_data['name'])
        self.platform_label.set_text(game_data['platform'])
        self.slug_label.set_text(game_data['slug'])
        
    def show_game_data(self,widget):
        window = GameData(game_data=self.game_data)
        
        
        

