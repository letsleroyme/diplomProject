import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def countNaN(col):
    k = 0
    for i in col:
        if (str)(i) == 'nan':
            k = k+1
    return k

def RemoveNanForCol(data, colNumber):
    return data.dropna(subset=[colNumber-1])

#---------------------для числовых значений-------------------------------
def GetMeanValueForCol(filename, colNumber, dt):
    data = np.genfromtxt(filename, dtype=dt, usecols=colNumber, delimiter=",", skip_header=1)
    return np.mean(data) if dt == float else int(np.mean(data))

def IsFloat(data):# если в столбце есть хоть один эл-т с точкой то флоат
    for i in data:
        if (str)(i) =='nan':
            continue
        if '.' in i:
            return True
        else:
            continue
    return False

def ReplaceNanForNumeric(data, colNumber, filename):# датасет, номер столбца, имя файла
    newdata = data.copy()
    df = float if IsFloat(data.iloc[:, colNumber-1]) else int
    mean = GetMeanValueForCol(filename, colNumber, df)
    newdata.iloc[:, colNumber-1] = data.iloc[:, colNumber-1].fillna(mean)
    return newdata# датасет
#-------------------------------------------------------------------------
#---------------------для категориальнх значений--------------------------
def GetTheMostCommonValueForCol(data, numcol):
    lst = data.iloc[:, numcol-1].value_counts().index.tolist()
    return lst[0]

def ReplaceNanForCategoric(data, colNumber):
    cv = GetTheMostCommonValueForCol(data, colNumber)
    k = 0
    newdata = data.copy()
    for i in data.iloc[:, colNumber - 1]:
        if (str)(i) == 'nan':
            newdata.iloc[k, colnum - 1] = cv
        k = k + 1
    return newdata

def ReplaceTextCategToNum(data, colNumber):
    newdata = data.copy()
    label = LabelEncoder()
    colwithoutNan = data.iloc[:, colNumber - 1].dropna()
    label.fit(colwithoutNan.drop_duplicates())
    #lst = list(label.classes_)  # ['C', 'Q', 'S']
    a = label.transform(colwithoutNan)
    k = 0
    for i in range(newdata.shape[0]):
        if (str)(newdata.iloc[i, colNumber - 1]) != 'nan':
            newdata.iloc[i, colNumber - 1] = a[k]
            k = k + 1
    return newdata
#-------------------------------------------------------------------------
#------------------------для текстовых значений---------------------------
def GetLowLetterForText(data, colNumber):
    newdata = data.copy()
    newdata.iloc[:, colNumber-1] = data.iloc[:, colNumber-1].str.lower()
    return newdata

def GetTextWithoutDots(data, colNumber):
    newdata = data.copy()
    newdata.iloc[:, colNumber-1] = newdata.iloc[:, colNumber-1].replace('[^a-zA-Z0-9]', ' ', regex=True)
    return newdata
#-------------------------------------------------------------------------
data = pd.read_csv('titanic.csv', header=None)
data = data.iloc[1:, :]
colnum = 4
#----------числовые------------
#newdata = ReplaceNanForNumeric(data, colnum, 'titanic.csv')
#print(newdata.iloc[60:70, 5:12])
#______________________________________________________________________________________________________________________
#--------категориальные--------
#print(ReplaceNanForCategoric(data, colnum).iloc[828:835,:])
#print(RemoveNanForCol(data, colnum).iloc[828:835,:])
#______________________________________________________________________________________________________________________
#-----------текстовые----------
#a = GetTextWithoutDots(data, colnum)
#a = GetLowLetterForText(a, colnum)
#print(a.iloc[:, 2: 5])delete flash:vlan.dat
#print(data.iloc[:, 2: 5])

def GetDict(data):
    dct = {}
    for i in range(data.shape[1]):
        dct[i+1] =(str)(i+1)+' ('+(str)(countNaN(data.iloc[:, i]))+' NaN)'
    return dct

def GetDictFromPandas(data):
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




