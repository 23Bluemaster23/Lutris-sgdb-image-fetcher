import gi
gi.require_version("Gtk","3.0")

from gi.repository import Gtk
import threading
from controllers.Fetching import FetchingController
from controllers.FileSystem import FileSystemController
from .WaitingDialog import WaitingDialog
class FetchingWindow(Gtk.Builder):
    
    def __init__(self,game_data) -> None:
        super().__init__()
        self.current_image = 0
        self.images = {}
        self.game_data = game_data
        self.add_from_file('templates/FetchingWindow.glade')
        self.window = self.get_object('FetchingWindow')
        self.game_flow = self.get_object('game_flow')
        
        
        self.window.show_all()
        self.fetch_images()
    def fetch_images(self):
        if self.current_image >2:
            FetchingController.save_images(self.images,self.game_data['slug'])
            self.window.destroy()
            return
        res = FetchingController.get_urls(self.game_data['id'],self.current_image)
 
        self.window.show_all()
        if res['success']:
            self.clear_flow()
            for item in res['data']:
                cell = ImageCell(item['thumb'],self.current_image)
                cell.image_button.connect('clicked',self.select_image,item['url'])
                self.game_flow.add(cell)
            
            self.window.show_all()
    def select_single_image(self,widget,url):
        self.images[self.game_data['type']] = url
        FetchingController.save_images(self.images,self.game_data['slug'])
    def clear_flow(self):
        children =self.game_flow.get_children()
        for child in children:
            self.game_flow.remove(child)
    def select_image(self,widget,url):
        if self.current_image<= 2:self.images[self.current_image] = url
        self.current_image +=1 
        self.fetch_images()
class ImageCell(Gtk.Box):
    def __init__(self,thumb,type):
        super().__init__()
        
        self.image_button = Gtk.Button(halign=Gtk.Align.CENTER,valign=Gtk.Align.CENTER,)
        self.image = Gtk.Image()
        self.image.set_from_pixbuf(FetchingController.get_image(thumb,type))
        self.image_button.set_image(self.image)
        self.pack_start(self.image_button,1,1,0)

class FetchingSingleWindow(FetchingWindow):
    def __init__(self, game_data) -> None:
        super().__init__(game_data)
        
    def fetch_images(self):
        res = FetchingController.get_urls(self.game_data['id'],self.game_data['type'])
 
        self.window.show_all()
        if res['success']:
            self.clear_flow()
            for item in res['data']:
                cell = ImageCell(item['thumb'],self.game_data['type'])
                cell.image_button.connect('clicked',self.select_image,item['url'])
                self.game_flow.add(cell)
            
            self.window.show_all()
    def select_image(self,widget,url):
        self.images[self.game_data['type']] = url
        FetchingController.save_images(self.images,self.game_data['slug'])
        self.window.destroy()