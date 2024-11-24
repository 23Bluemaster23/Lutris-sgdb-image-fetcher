import gi

gi.require_version('Gtk','3.0')
import threading
from gi.repository import Gtk
from controllers.Fetching import FetchingController

class SearchWindow(Gtk.Builder):
    def __init__(self,game_name,parent):
        super().__init__()
        self.game_name = game_name
        self.parent = parent
        self.add_from_file('templates/SearchWindow.glade')
        handlers = {
            'on_seach_button_clicked':self.search_game_action,
            'on_SearchWindow_destroy':self.parent.fetch_images_action
        }
        self.connect_signals(handlers)
        self.window = self.get_object('SearchWindow')
        self.search_entry:Gtk.Entry = self.get_object('search_entry') 
        self.search_entry.set_text(self.game_name)
        self.game_list:Gtk.Box = self.get_object('game_list')
        self.seleted_id = ''
        
        self.window.set_modal(True)
        self.window.show_all()
    
    def search_game_action(self,widget):
        x = threading.Thread(target=self.search_game)
        x.start()
        
    def search_game(self):
        res = FetchingController.get_game(self.search_entry.get_text())
        children = self.game_list.get_children()
        for child in children:
            self.game_list.remove(child)
        for item in res['data']:
            row = SearchRow(item,self.window)
            self.game_list.pack_start(row.widget,0,1,0)
class SearchRow(Gtk.Builder):
    def __init__(self,game_data,parent):
        super().__init__()
        self.parent = parent
        self.add_objects_from_file('templates/SearchRow.glade',['game_row'])
        self.widget = self.get_object('game_row')
        handlers = {
            'on_edit_button_clicked': self.select_game,
        }
        self.connect_signals(handlers)
        self.name_label:Gtk.Label = self.get_object('name_label')
        self.id_label:Gtk.Label = self.get_object('id_label')
        self.platform_label:Gtk.Label = self.get_object('platform_label')
        
        self.name_label.set_text(game_data['name'])
        self.id_label.set_text(str(game_data['id']))
    
    def select_game(self,widget):
        self.parent.selected_id = self.id_label.get_text()
        self.parent.destroy()
        
class SearchSingleWindow(Gtk.Builder):
    def __init__(self,game_name,parent):
        super().__init__()
        self.game_name = game_name
        self.parent = parent
        self.add_from_file('templates/SearchSingleWindow.glade')
        handlers = {
            'on_seach_button_clicked':self.search_game_action,
            'on_SearchWindow_destroy':self.parent.fetch_single_image_action
        }
        self.connect_signals(handlers)
        self.window = self.get_object('SearchWindow')
        self.search_entry:Gtk.Entry = self.get_object('search_entry') 
        self.search_entry.set_text(self.game_name)
        self.game_list:Gtk.Box = self.get_object('game_list')
        self.seleted_id = ''
        
        self.window.set_modal(True)
        self.window.show_all()
        
    def search_game_action(self,widget):
        x = threading.Thread(target=self.search_game)
        x.start()
        
    def search_game(self):
        res = FetchingController.get_game(self.search_entry.get_text())
        children = self.game_list.get_children()
        for child in children:
            self.game_list.remove(child)
        for item in res['data']:
            row = SearchRow(item,self.window)
            self.game_list.pack_start(row.widget,0,1,0)