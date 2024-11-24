import requests
import json
import urllib3
import gi
gi.require_version("Gtk","3.0")
from .Config import ConfigModel
from constants.CONSTANTS import ImageSize,FullImageSize
from gi.repository import GdkPixbuf,Gio
headers = {
        'Authorization': 'Bearer {0}'.format(ConfigModel.get_config('FETCHING','api_key')),

        }

class FetchingModel():
    @staticmethod
    def get_game(query):

        url = 'https://www.steamgriddb.com/api/v2/search/autocomplete/{0}?limit=10'.format(query)
        response = requests.get(url,headers=headers)
        return json.loads(response.text)
    
    @staticmethod
    def get_icon(id):
        url = 'https://www.steamgriddb.com/api/v2/icons/game/{0}?limit=10'.format(id)
        response = requests.get(url,headers=headers)
        return json.loads(response.text)
    @staticmethod
    def get_covertart(id):
        url = 'https://www.steamgriddb.com/api/v2/grids/game/{0}?dimensions=342x482,600x900&limit=10'.format(id)
        response = requests.get(url,headers=headers)
        return json.loads(response.text)
    @staticmethod
    def get_banner(id):
        url = 'https://www.steamgriddb.com/api/v2/grids/game/{0}?dimensions=920x430,460x215&limit=10'.format(id)
        response = requests.get(url,headers=headers)
        return json.loads(response.text)
    @staticmethod
    def get_icon_image(url):
        res = requests.get(url)
        width,height = ImageSize.ICON.values()
        imput_stream = Gio.MemoryInputStream.new_from_data(res.content,None)
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(imput_stream,width=width,height=height,preserve_aspect_ratio=True)
        return pixbuf
    @staticmethod
    def get_full_icon_image(url):
        res = requests.get(url)
        width,height = FullImageSize.ICON.values()
        imput_stream = Gio.MemoryInputStream.new_from_data(res.content,None)
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(imput_stream,width=width,height=height,preserve_aspect_ratio=False)
        return pixbuf
    @staticmethod
    def get_coverart_image(url):
        res = requests.get(url)
        width,height = ImageSize.COVERTART.values()
        imput_stream = Gio.MemoryInputStream.new_from_data(res.content,None)
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(imput_stream,width=width,height=height,preserve_aspect_ratio=True)
        return pixbuf
    @staticmethod
    def get_full_coverart_image(url):
        res = requests.get(url)
        width,height = FullImageSize.COVERTART.values()
        imput_stream = Gio.MemoryInputStream.new_from_data(res.content,None)
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(imput_stream,width=width,height=height,preserve_aspect_ratio=False)
        return pixbuf
    @staticmethod
    def get_banner_image(url):
        res = requests.get(url)
        width,height = ImageSize.BANNER.values()
        imput_stream = Gio.MemoryInputStream.new_from_data(res.content,None)
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(imput_stream,width=width,height=height,preserve_aspect_ratio=True)
        return pixbuf
    @staticmethod
    def get_full_banner_image(url):
        res = requests.get(url)
        width,height = FullImageSize.BANNER.values()
        imput_stream = Gio.MemoryInputStream.new_from_data(res.content,None)
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(imput_stream,width=width,height=height,preserve_aspect_ratio=False)
        return pixbuf
""" if __name__ == '__main__':
    res = FetchingModel.get_icon('37177')
    
    for item in res['data']:
        print(item['url']) """