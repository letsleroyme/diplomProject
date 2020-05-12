from flask import Flask, request, jsonify, g, session
from flask_cors import CORS
import pandas as pd
import json
from ProcessData import *



app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8' #!!! секретный ключ, нужен для нормальной работы сессии


@app.route("/", methods=['GET','POST'])
def upload():
    f = request.files['file']
    fileName = f.filename
    fort = fileName.split(".")
    session['filename'] = f.filename
    if fort[1] != 'csv':
        response = jsonify({'status': 415, 'error': 'Unsupported Media Type',
                            'message': 'Wrong type of file'})
        response.status_code = 415
        return response
    f.save('C:\\github\\diplomNew\\diplomProject\\Back\\' + fileName)
    data = pd.read_csv('C:\\github\\diplomNew\\diplomProject\\Back\\titanic.csv', header=None)
    #data = pd.read_csv('titanic.csv', header=None)
    #g.ddata = data
    #session['abc'] = f.filename  # !!! записываю в сессию имя файла
    dct = GetDictTable(data)
    return jsonify(dct)

@app.route("/table", methods=['GET','POST'])
def tbl():
    result = dataProcessing(request)
    return result
    # filename = 'titanic.csv'
    # data = pd.read_csv('C:\\github\\diplomNew\\diplomProject\\Back\\titanic.csv', header=None)
    # data = data.iloc[0:, :]
    # print(var.name)
    # if request.method == 'POST':
    #     requestDict = request.get_json(force=True)
    #     ListOfNumCols = GetNumListOfColumn(requestDict['numberColumns'])
    #     ListOfCatCols = GetNumListOfColumn(requestDict['categoricalColumns'])
    #     ListOfTextCols = GetNumListOfColumn(requestDict['textDataColumns'])

    #     outdata = data.copy()
    #     if requestDict['action1_check1']:
    #         outdata = ReplaceNanForNumeric(outdata, ListOfNumCols, filename)

    #     if requestDict['action1_check2']:
    #         outdata = RemoveNanForCol(outdata, ListOfNumCols)

    #     if requestDict['action2_check1']:
    #         outdata = ReplaceNanForCategoric(outdata, ListOfCatCols)

    #     if requestDict['action2_check2']:
    #         outdata = RemoveNanForCol(outdata, ListOfCatCols)

    #     if requestDict['action2_check3']:
    #         outdata = ReplaceTextCategToNum(outdata, ListOfCatCols)

    #     if requestDict['action3_check1']:
    #         outdata = GetLowLetterForText(outdata, ListOfTextCols)

    #     if requestDict['action3_check2']:
    #         outdata = GetTextWithoutDots(outdata, ListOfTextCols)

    #     if requestDict['action3_check3']:
    #         outdata = RemoveNanForCol(outdata, ListOfTextCols)

    #     response = GetDictTable(outdata)
    #     return jsonify(response)
    # else:
    #     return jsonify(GetDictColumns(data))# вернуть список столбцов в виде джсон


def dataProcessing(request): 
    filename = 'C:\\github\\diplomNew\\diplomProject\\Back\\titanic.csv'
    data = pd.read_csv('C:\\github\\diplomNew\\diplomProject\\Back\\titanic.csv', header=None)
    data = data.iloc[0:, :]

    if request.method == 'POST':
        requestDict = request.get_json(force=True)
        ListOfNumCols = GetNumListOfColumn(requestDict['numberColumns'])
        ListOfCatCols = GetNumListOfColumn(requestDict['categoricalColumns'])
        ListOfTextCols = GetNumListOfColumn(requestDict['textDataColumns'])

        outdata = data.copy()
        if requestDict['action1_check1']:
            outdata = ReplaceNanForNumeric(outdata, ListOfNumCols, filename)

        if requestDict['action1_check2']:
            outdata = RemoveNanForCol(outdata, ListOfNumCols)

        if requestDict['action2_check1']:
            outdata = ReplaceNanForCategoric(outdata, ListOfCatCols)

        if requestDict['action2_check2']:
            outdata = RemoveNanForCol(outdata, ListOfCatCols)

        if requestDict['action2_check3']:
            outdata = ReplaceTextCategToNum(outdata, ListOfCatCols)

        if requestDict['action3_check1']:
            outdata = GetLowLetterForText(outdata, ListOfTextCols)

        if requestDict['action3_check2']:
            outdata = GetTextWithoutDots(outdata, ListOfTextCols)

        if requestDict['action3_check3']:
            outdata = RemoveNanForCol(outdata, ListOfTextCols)

        response = GetDictTable(outdata)
        return jsonify(response)
    else:
        return jsonify(GetDictColumns(data))    

if __name__ == "__main__":
    app.run(debug = True)


