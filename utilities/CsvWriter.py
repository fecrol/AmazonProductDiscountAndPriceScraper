from genericpath import exists
from os.path import exists
import pandas as pd

class CsvWriter:
    
    def append_to_csv(self, filename, data, column_names):

        df = pd.DataFrame(data, columns=column_names)
        
        if(exists(filename)):
            df.to_csv(filename, mode="a", encoding="utf-8", index=False, header=False)
            print("File found, appending...")
        else:
            df.to_csv(filename, encoding="utf-8", index=False)
            print("File not found, creating...")