from models.Config import ConfigModel


class ConfigController():
    
    def get_config(section:str,key:str):
        return ConfigModel.get_config(section,key)
    
    def set_config(section:str,key:str,value:any):
        return ConfigModel.set_config(section,key,value)
    
    def write_config():
        res  = ConfigModel.write_config()
        return 0