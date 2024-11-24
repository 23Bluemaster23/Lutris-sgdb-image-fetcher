import gi
gi.require_version("Gtk","3.0")
from gi.repository import GdkPixbuf
from models.Fetching import FetchingModel
from models.FileSystem import FileSystemModel
from constants.CONSTANTS import FileType

class FetchingController():
    @staticmethod
    def get_game(query:str):
        return FetchingModel.get_game(query)
    @staticmethod
    def get_urls(id,type):
        match type:
            case FileType.ICON:
                return FetchingModel.get_icon(id)
            case FileType.COVERTART:
                return FetchingModel.get_covertart(id)
            case FileType.BANNER:
                return FetchingModel.get_banner(id)
    @staticmethod
    def get_image(url,type):
        
        match type:
            case FileType.ICON:
                return FetchingModel.get_icon_image(url)
            case FileType.COVERTART:
                return FetchingModel.get_coverart_image(url)
            case FileType.BANNER:
                return FetchingModel.get_banner_image(url)
    @staticmethod
    def save_images(images:dict,slug):
        image:GdkPixbuf.Pixbuf
        type:str
        
        for key,value in images.items():
            filename = FileSystemModel.get_filename(key,slug)
            type = ''
            match key:
                case FileType.ICON:
                    image = FetchingModel.get_full_icon_image(value)
                    type = 'png'
                case FileType.COVERTART:
                    image = FetchingModel.get_full_coverart_image(value)
                    type = 'jpeg'
                case FileType.BANNER:
                    image = FetchingModel.get_full_banner_image(value)
                    type = 'jpeg'
            image.savev(filename=filename,type=type)