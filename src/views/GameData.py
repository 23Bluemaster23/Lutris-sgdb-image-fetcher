import gi

gi.require_version('Gtk','3.0')

from gi.repository import Gtk
from .SearchWindow import SearchSingleWindow, SearchWindow
from .FetchingWindow import FetchingSingleWindow, FetchingWindow
from controllers.FileSystem import FileSystemController
from constants.CONSTANTS import FileType
class GameData(Gtk.Builder):
    def __init__(self,game_data:dict):
        super().__init__()
        self.game_data = game_data
        self.add_from_file('templates/GameData.glade')
        handlers = {
            'on_fetch_button_clicked':self.search_image,
            'on_icon_button_clicked':self.fetch_icon_image,
            'on_banner_button_clicked':self.fetch_banner_image,
            'on_coverart_button_clicked':self.fetch_coverart_image
        }
        self.selected_id = ''
        self.type = 0
        self.connect_signals(handlers)
        self.window = self.get_object('GameData')
        self.name_label:Gtk.Label = self.get_object('name_label')
        self.name_label.set_text(self.game_data['name'])
        self.banner_image:Gtk.Image = self.get_object('banner_image')
        self.coverart_image:Gtk.Image = self.get_object('coverart_image')
        self.icon_image:Gtk.Image = self.get_object('icon_image')
        self.banner_image.set_from_pixbuf(FileSystemController.get_image(FileType.BANNER,self.game_data['slug']))
        self.coverart_image.set_from_pixbuf(FileSystemController.get_image(FileType.COVERTART,self.game_data['slug']))
        self.icon_image.set_from_pixbuf(FileSystemController.get_image(FileType.ICON,self.game_data['slug']))
        self.window.set_modal(True)
        self.window.show_all()

    def search_image(self,widget):
        window = SearchWindow(self.game_data['name'],self)
    def fetch_coverart_image(self,widget):
        self.type = FileType.COVERTART
        window = SearchSingleWindow(self.game_data['name'],self)
    def fetch_icon_image(self,widget):
        self.type = FileType.ICON
        window = SearchSingleWindow(self.game_data['name'],self)
    def fetch_banner_image(self,widget):
        self.type = FileType.BANNER
        window = SearchSingleWindow(self.game_data['name'],self)
    def fetch_images_action(self,widget):
        if hasattr(widget, 'selected_id'):
            self.window.set_modal(False)
            window = FetchingWindow({'id':widget.selected_id,'slug':self.game_data['slug'],'type':self.type})
    
    def fetch_single_image_action(self,widget):
        if hasattr(widget, 'selected_id'):
            self.window.set_modal(False)
            window = FetchingSingleWindow({'id':widget.selected_id,'slug':self.game_data['slug'],'type':self.type})