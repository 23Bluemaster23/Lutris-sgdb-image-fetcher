import gi
gi.require_version("Gtk","3.0")
from configparser import Error
from .Config import ConfigModel
from gi.repository import GdkPixbuf
from constants.CONSTANTS import FileType,ImageSize
import os

class FileSystemModel():
    @staticmethod
    def get_image(type:int,slug):
        pre = ''
        path = ''
        ext = ''
        width = 0
        height = 0
        match type:
            case FileType.ICON:
                path = ConfigModel.get_config('LOCATIONS','icon')
                pre = 'lutris_'
                ext = '.png'
                width,height = ImageSize.ICON.values()
            case FileType.BANNER:
                path = ConfigModel.get_config('LOCATIONS','banner')
                ext = '.jpg'
                width,height = ImageSize.BANNER.values()
            case FileType.COVERTART:
                path = ConfigModel.get_config('LOCATIONS','coverart')
                ext = '.jpg'
                width,height = ImageSize.COVERTART.values()
        filepath = os.path.join(path,pre+slug+ext)
        try:
            image = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=filepath,
                width=width,
                height=height,
                preserve_aspect_ratio=True
            )
        except Exception as e:
            return 
        return image
    @staticmethod
    def get_filename(type:int,slug):
        pre = ''
        path = ''
        ext = ''
        width = 0
        height = 0
        match type:
            case FileType.ICON:
                path = ConfigModel.get_config('LOCATIONS','icon')
                pre = 'lutris_'
                ext = '.png'
            case FileType.BANNER:
                path = ConfigModel.get_config('LOCATIONS','banner')
                ext = '.jpg'
            case FileType.COVERTART:
                path = ConfigModel.get_config('LOCATIONS','coverart')
                ext = '.jpg'
        return os.path.join(path,pre+slug+ext)