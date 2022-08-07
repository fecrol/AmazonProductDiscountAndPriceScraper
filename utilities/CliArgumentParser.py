import sys
import json

class CliArgumentParser:

    def get_args_as_dict(self):

        try:
            args_as_string = sys.argv[1].replace("'", "\"")
            args_as_dict = json.loads(args_as_string)

            return args_as_dict
        except:
            print("An error has occured")
