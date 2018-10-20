import csv
import ast
import os
import shutil
import dateutil.parser
def get_data_set():
    '''We have to convert it into a "understandable format. So we have to clean it up, because alot of the tiles is not unicode based right.'''
    with open(os.getcwd() + '\\uforeports.csv', encoding="utf8", errors='ignore') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data_set = []
        for row in reader:
                try:
                    # We create a single object for each row, that takes the important informations and put them into an array.
                    row_object = {}
                    # Had to decode some characters into a suitable format the computer understands, so we chose to use latin. We also put the information into suitable formats, for better performance and correct indication
                    row_object['year'] = int(row[0:1][0].split(' ')[0][-4:])
                    row_object['month'] = int(row[0:1][0].split('/')[0])
                    row_object['place'] = row[1:2][0]
                    row_object['shape'] = row[4:5][0]
                    row_object['duration'] = int(row[5:6][0])
                    
                    data_set.append(row_object)
                except:
                    pass
    return data_set