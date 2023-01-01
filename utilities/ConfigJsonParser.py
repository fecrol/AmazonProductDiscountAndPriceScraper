import json

class ConfigJsonParser:

    def __init__(self):
        self.__config_data = self.__read_json_config()

    def __read_json_config(self):

        try:
            config_file = open("./config.json")
            config_data = json.load(config_file)

            return config_data
        except:
            print("An error has occured")
            return
    
    def get_config_data(self):

        return self.__config_data