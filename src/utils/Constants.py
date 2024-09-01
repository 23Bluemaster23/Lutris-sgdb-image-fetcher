from enum import Enum


class ImageType(Enum):
    JPG = "JPG"
    PNG = "PNG"


class ImageRes(Enum):
    COVERART = (264, 352)
    BANNER = (184, 69)
    ICON = (128, 128)


class FilenameTemplate(Enum):
    COVERART = "{slug}.jpg"
    BANNER = "{slug}.jpg"
    ICON = "lutris_{slug}.png"
