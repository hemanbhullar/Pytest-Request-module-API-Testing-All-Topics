import json
import csv
import openpyxl


#JSON Data Provider
def read_json_data(filepath):
    with open(filepath, 'r') as f:
        data_list = json.load(f)
    return [(item,)for item in data_list]


#CSV Data Provider
def read_csv_data(filepath):
    data_l = []
    with open(filepath, 'r') as f:
        data_list = csv.reader(f)
        next(data_list)
        for row in data_list:
            data_l.append(tuple(row))

    return data_l