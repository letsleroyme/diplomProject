import numpy as np
from flask import jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def countNaN(col):
    k = 0
    for i in col:
        if (str)(i) == 'nan':
            k = k+1
    return k

def RemoveNanForCol(data, colList):
    return data.dropna(subset=(a-1 for a in colList))

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def CheckNumericType(data, colList):
    lst = []
    newdata = data.dropna()
    for col in colList:
        for i in newdata.iloc[:, col-1]:
            if not is_digit((str)(i)):
                lst.append(col)
                break
    return lst

def TurnToString(data):
    newdata = data.copy()
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if type(data.iloc[i, j]) != str:
                newdata.iloc[i, j] = (str)(data.iloc[i, j])
    return newdata


def ProcessCheckBoxes(data, checkboxes, filename):
    ListOfNumCols = GetNumListOfColumn(checkboxes['numberColumns'])
    notNumericList = CheckNumericType(data, ListOfNumCols)
    if notNumericList:
        numstr = ''
        for i in notNumericList:
            numstr = numstr + (str)(i) + ', '
        response = jsonify({'status': 405, 'error': 'Method Not Allowed',
                            'message': 'Chosen column ' + numstr + ' - is not numeric and not allowed to process'})
        response.status_code = 405
        return 1, response
    ListOfCatCols = GetNumListOfColumn(checkboxes['categoricalColumns'])
    ListOfTextCols = GetNumListOfColumn(checkboxes['textDataColumns'])
    outdata = data.copy()
    if checkboxes['action1_check1']:
        outdata = ReplaceNanForNumeric(outdata, ListOfNumCols, filename)
    if checkboxes['action1_check2']:
        outdata = RemoveNanForCol(outdata, ListOfNumCols)
    if checkboxes['action2_check1']:
        outdata = ReplaceNanForCategoric(outdata, ListOfCatCols)
    if checkboxes['action2_check2']:
        outdata = RemoveNanForCol(outdata, ListOfCatCols)
    if checkboxes['action2_check3']:
        outdata = ReplaceTextCategToNum(outdata, ListOfCatCols)
    if checkboxes['action3_check1']:
        outdata = GetLowLetterForText(outdata, ListOfTextCols)
    if checkboxes['action3_check2']:
        outdata = GetTextWithoutDots(outdata, ListOfTextCols)
    if checkboxes['action3_check3']:
        outdata = RemoveNanForCol(outdata, ListOfTextCols)
    return 0, outdata

def GetTableAfterPreProcessing(data, checkboxes, filename, header):
    i, outdata = ProcessCheckBoxes(data, checkboxes, filename)  # обработанный датасет
    if i:#если есть ошибка
        return outdata, i
    outdata = TurnToString(outdata)
    return pd.concat([header, outdata], axis=0) if len(header) else outdata, i

#---------------------для числовых значений-------------------------------
def GetMeanValueForCol(filename, colNumber, dt):
    data = np.genfromtxt(filename, dtype=float, usecols=colNumber, delimiter=",", skip_header=1)
    return round(np.nanmean(data), 3) if dt == float else int(np.nanmean(data))

def IsFloat(data):# если в столбце есть хоть один эл-т с точкой то флоат
    for i in data:
        if (str)(i) =='nan':
            continue
        if '.' in i:
            return True
    return False

def ReplaceNanForNumeric(data, colList, filename):# датасет, номер столбца, имя файла
    newdata = data.copy()
    for i in colList:
        if(countNaN(newdata.iloc[:, i-1])):
            df = float if IsFloat(data.iloc[:, i-1]) else int
            mean = GetMeanValueForCol(filename, i, df)
            newdata.iloc[:, i-1] = data.iloc[:, i-1].fillna(mean)
    return newdata# датасет
#-------------------------------------------------------------------------
#---------------------для категориальных значений--------------------------
def GetTheMostCommonValueForCol(data, numcol):
    lst = data.iloc[:, numcol-1].value_counts().index.tolist()
    return lst[0]

def ReplaceNanForCategoric(data, colList):
    newdata = data.copy()
    for colnum in colList:
        if countNaN(newdata.iloc[:, colnum - 1]):
            cv = GetTheMostCommonValueForCol(data, colnum)
            k = 0
            for i in data.iloc[:, colnum - 1]:
                if str(i) == 'nan':
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
#-------------------------------------------------------------------------

def GetDictColumns(data, fl):
    dct = {}
    for i in range(data.shape[1]):
        dct[i+1] =(str)(i+1)+' ('+(str)(countNaN(data.iloc[:, i]))+' NaN)' if fl else (str)(i+1)
    return dct


#cols = pivotTable.columns.tolist()#male/fem/survived/died
       # responseDct['labels'] = pivotTable.index.tolist()# 1, 2, 3 класс
def ReplaceNaNTo(data, sym):
    newdata = data.copy()
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if (str)(data.iloc[i, j]) == 'nan':
                newdata.iloc[i, j] = sym
    return newdata


def GetDictTable(data):
    cols = data.shape[1]
    rows = data.shape[0]
    a = [c for c in range(0, cols+1)]
    d = {}
    d[0] = a
    data = ReplaceNaNTo(data, "NaN")
    for i in range(1, rows+1):
        lst = []
        lst.append(i)
        for j in range(cols):
            lst.append(data.iloc[i-1, j])
        d[i] = lst
    return d

def GetNumListOfColumn(lst):
    outlst=[]
    for i in lst:
        outlst.append((int)(i.split(" ")[0]))
    return outlst

def GetDataForCharts(requestData, data):
    responseDct = {}
    dataDict={}
    data = TurnToString(data)
    for key, value in requestData.items():
        if value == True:
            responseDct['GraphType'] = key.split("s")[1]
    if responseDct['GraphType'] == 'StackedBar':
        colX = (int)(requestData['columnX'][0])
        colY = (int)(requestData['columnY'][0])
        pivotTable = ReplaceNaNTo(data.groupby([colX-1, colY-1]).size().unstack(), 0)
        cols = pivotTable.columns.tolist()
        responseDct['labels'] = pivotTable.index.tolist()
        responseDct['header'] = cols
        for i in range(len(cols)):
            dataDict[i] = pivotTable.iloc[:, i].values.tolist()
        responseDct['data'] = dataDict
    else:
        labelDct = {}
        dataDct = {}
        headDct = {}
        numcol = (int)(requestData['selectColumn'][0])
        values = sorted(data.iloc[:, numcol - 1].value_counts().index.tolist())# labels
        amountOfValues = data.groupby([numcol - 1]).size().tolist()# data
        labelDct[1] = values
        dataDct[1] = amountOfValues
        headDct[1] = 'Column #'+ (str)(numcol)
        responseDct['labels'] = labelDct
        responseDct['data'] = dataDct
        responseDct['header'] = headDct
    return responseDct
