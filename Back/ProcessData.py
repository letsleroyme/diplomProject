import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def countNaN(col):
    k = 0
    for i in col:
        if (str)(i) == 'nan':
            k = k+1
    return k

def RemoveNanForCol(data, colList):
    newlist = (a-1 for a in colList)
    return data.dropna(subset=newlist)

#---------------------для числовых значений-------------------------------
def GetMeanValueForCol(filename, colNumber, dt):
    data = np.genfromtxt(filename, dtype=float, usecols=colNumber, delimiter=",", skip_header=1)
    return np.nanmean(data) if dt == float else int(np.nanmean(data))

def IsFloat(data):# если в столбце есть хоть один эл-т с точкой то флоат
    for i in data:
        if (str)(i) =='nan':
            continue
        if '.' in i:
            return True
        else:
            continue
    return False

def ReplaceNanForNumeric(data, colList, filename):# датасет, номер столбца, имя файла
    newdata = data.copy()
    for i in colList:
        df = float if IsFloat(data.iloc[:, i-1]) else int
        mean = GetMeanValueForCol(filename, i, df)
        newdata.iloc[:, i-1] = data.iloc[:, i-1].fillna(mean)
    return newdata# датасет
#-------------------------------------------------------------------------
#---------------------для категориальнх значений--------------------------
def GetTheMostCommonValueForCol(data, numcol):
    lst = data.iloc[:, numcol-1].value_counts().index.tolist()
    return lst[0]

def ReplaceNanForCategoric(data, colList):
    newdata = data.copy()
    for colnum in colList:
        cv = GetTheMostCommonValueForCol(data, colnum)
        k = 0
        for i in data.iloc[:, colnum - 1]:
            if (str)(i) == 'nan':
                newdata.iloc[k, colnum - 1] = cv
            k = k + 1
    return newdata

def ReplaceTextCategToNum(data, colList):
    newdata = data.copy()
    for numcol in colList:
        label = LabelEncoder()
        colwithoutNan = newdata.iloc[:, numcol - 1].dropna()
        label.fit(colwithoutNan.drop_duplicates())
        #lst = list(label.classes_)  # ['C', 'Q', 'S']
        a = label.transform(colwithoutNan)
        k = 0
        for i in range(newdata.shape[0]):
            if (str)(newdata.iloc[i, numcol - 1]) != 'nan':
                newdata.iloc[i, numcol - 1] = (str)(a[k])
                k = k + 1
    return newdata
#-------------------------------------------------------------------------
#------------------------для текстовых значений---------------------------
def GetLowLetterForText(data, colList):
    newdata = data.copy()
    for i in colList:
        newdata.iloc[:, i-1] = newdata.iloc[:, i-1].str.lower()
    return newdata

def GetTextWithoutDots(data, colList):
    newdata = data.copy()
    for i in colList:
        newdata.iloc[:, i-1] = newdata.iloc[:, i-1].replace('[^a-zA-Z0-9]', ' ', regex=True)
    return newdata

def GetDictColumns(data):
    dct = {}
    for i in range(data.shape[1]):
        dct[i+1] =(str)(i+1)+' ('+(str)(countNaN(data.iloc[:, i]))+' NaN)'
    return dct

def GetDictTable(data):
    cols = data.shape[1]
    rows = data.shape[0]
    a = [c for c in range(0, cols+1)]
    d = {}
    d[0] = a
    for i in range(1, rows+1):
        lst = []
        lst.append(i)
        for j in range(cols):
            if (str)(data.iloc[i-1, j]) == 'nan':
                lst.append("NaN")
            else:
                lst.append(data.iloc[i-1, j])
        d[i] = lst
    return d

def GetNumListOfColumn(lst):
    outlst=[]
    for i in lst:
        outlst.append((int)(i.split(" ")[0]))
    return outlst