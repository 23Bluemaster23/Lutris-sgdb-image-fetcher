import configparser
import os

from .Constants import FilenameTemplate


__parser = configparser.ConfigParser()
__parser.read("config.ini")


def update_parser():
    try:
        pass
    except configparser.Error as e:
        print(e.message)


def get_config(
    section: str,
    option: str,
):
    return __parser.get(section=section, option=option)


def set_config(section: str, option: str, value: str):
    __parser.set(section=section, option=option, value=value)


def get_filename(type: str, slug: str):
    file_name = FilenameTemplate[type.upper()].value.format(slug=slug)
    file_name = os.path.join(__parser.get(section="LOCATIONS", option=type), file_name)

    return file_name


def get_all_options_of_section(section: str):
    return __parser.items(section=section)


def save_config():
    with open("config.ini", "w") as configfile:
        __parser.write(configfile)


# if __name__ == "__main__":
#     parser = ConfigParser()
#     print(parser.get_filename("banner", "super-mario-64"))
