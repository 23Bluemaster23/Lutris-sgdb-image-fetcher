import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class ConfigModel():
    @staticmethod
    def get_config(section:str,key:str):
        return config.get(section,key)
    @staticmethod
    def set_config(section:str,key:str,value):
        return config.set(section,key,value)
    @staticmethod
    def write_config():
        with open('config.ini','w') as configFile:
            config.write(configFile)

