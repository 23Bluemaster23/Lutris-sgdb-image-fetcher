from models.FileSystem import FileSystemModel


class FileSystemController():
    @staticmethod
    def get_image(type:int,slug:str):
        return FileSystemModel.get_image(type,slug)