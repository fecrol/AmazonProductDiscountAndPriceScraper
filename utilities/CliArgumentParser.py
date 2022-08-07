import sys
import json

class CliArgumentParser:

    def __init__(self):
        
        try:
            self.__args_as_string = sys.argv[1].replace("'", "\"")
            self.__args_as_dict = json.loads(self.__args_as_string)
        except:
            print("An error has occured")
            sys.exit()
    
    def get_url(self):
        """
        Mandatory command line argument needed to run the script
        """

        try:
            return self.__args_as_dict["url"]
        except:
            print("Error: No URL found in the list of arguments")
            sys.exit()
    
    def get_csv_filename(self):
        """
        Mandatory command line argument needed to run the script
        """

        try:
            return self.__args_as_dict["csv-filename"]
        except:
            print("Error: No CSV Filename found in list of arguments")
            sys.exit()