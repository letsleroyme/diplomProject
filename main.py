from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json
from ProcessData import *
import pathlib

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "https://diplom-front.herokuapp.com/"
    }
})

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    pdData = None
    header = None
    filename = None

@app.route("/", methods=['POST'])
def upload():
    f = request.files['file']
    fileName = f.filename
    check = request.form.get('check')
    fort = fileName.split(".")
    if fort[1] != 'csv':
        response = jsonify({'status': 415, 'error': 'Unsupported Media Type',
                            'message': 'Wrong type of file'})
        response.status_code = 415
        return response
    #f.save('C:\\Users\\Дарья\\Desktop\\Диплом\\diplomProject\\Back\\' + fileName)
    f.save(str(pathlib.Path(__file__).parent.absolute()) + '\\' + fileName)
    data = pd.read_csv(fileName, header=None)
    s1 = Singleton()
    s1.pdData = data.iloc[1:, :] if check else data
    s1.header = pd.DataFrame(data.iloc[0, :]).transpose() if check else None
    s1.filename = fileName
    dct = GetDictTable(pd.concat([s1.header, s1.pdData], axis=0))
    return dct

@app.route("/table", methods=['GET','POST'])
def tbl():
    s2 = Singleton()
    data = s2.pdData
    if request.method == 'POST':
        requestDict = request.get_json(force=True)# ответ с фронта
        outdata, isError = GetTableAfterPreProcessing(data, requestDict, s2.filename, s2.header)# обработанный датасет
        s2.pdData = outdata.iloc[1:, :] if len(s2.header) else outdata
        return outdata if isError else GetDictTable(outdata)
    else:
        return GetDictColumns(data, 1)


@app.route("/graphs", methods=['GET','POST'])
def graph():
    s3 = Singleton()
    data = s3.pdData
    if request.method == 'POST':
        requestData = request.get_json(force=True)
        return GetDataForCharts(requestData, data)
    else:
        return GetDictColumns(data, 0)


if __name__ == "__main__":
    app.run()


