from exceptions import *

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    try:
        with open(filepath, 'r') as file:
            # initialize list that will hold all the entries
            fileContentList = []
            entryDict = {}
            # for every line in the file
            
            for i, line in enumerate(file):
            
                # for the first line of every file, there will be data that shows the keys for each column.
                # this block will create a dictionary using those key names, and the dictionary will
                # act as a template for each entry
                entry = line.split(",")[:-1]
                if i == 0:
                    for newKey in entry:
                        entryDict[newKey] = None
                        continue
                
                counter = 0
                for key in entryDict:
                    entryDict[key] = entry[counter]
                    counter += 1
                fileContentList.append(entryDict)
                
    except FileNotFoundError as e:
        print(f"Error: {e}. Did you give the correct file name?")
        raise FileProcessingError
    except UnicodeDecodeError as e:
        print(f"Error: {e}. You really screwed up this time.")
    return fileContentList