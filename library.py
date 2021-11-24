import csv

def loadList(fileName, newLine = ''): 
    with open(fileName) as csv_file: 
        reader = csv.reader(csv_file)
        dataList = list(reader)
    return dataList
