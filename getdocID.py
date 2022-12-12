import pandas as pd
import os

def getDocID():
    #make sure that there is only one excel sheet in the directory
    excelset = set()
    for i in os.listdir():
        if i[-5:] == '.xlsx':
            excelset.add(i)

    #we are good to go
    if len(excelset) == 1:
        excelname = excelset.pop()

    try:
        excel = pd.read_excel(excelname)
    except NameError:
        print('You might have put more than one excel sheet in the folder ')
    
    ziplist = list(zip(excel['DocID'],excel['File Name'],excel['File Type']))
    return ziplist