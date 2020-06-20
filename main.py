from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
import pandas as pd
import json
from ProcessData import *
from sndbox import *
import pathlib
from corsFIX import *
import os, getpass, platform

app = Flask(__name__)
CORS(app, resources=r'/*')

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    pdData = None
    header = None
    filename = None
    requestData = None


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')

  return response

@app.route("/", methods=['POST'])
#@crossdomain(origin='*')
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
    f.save(str(pathlib.Path(__file__).parent.absolute()) + '/' + fileName)
    data = pd.read_csv(fileName, header=None)
    s1 = Singleton()
    s1.pdData = data.iloc[1:, :] if check else data
    s1.header = pd.DataFrame(data.iloc[0, :]).transpose() if check else None
    s1.filename = fileName
    dct = GetDictTable(pd.concat([s1.header, s1.pdData], axis=0))
    return dct

@app.route("/table", methods=['GET','POST'])
#@crossdomain(origin='*')
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
#@crossdomain(origin='*')
def graph():
    s3 = Singleton()
    data = s3.pdData
    if request.method == 'POST':
        requestData = request.get_json(force=True)
        return GetDataForCharts(requestData, data)
    else:
        return GetDictColumns(data, 0)
 
@app.route("/request", methods=['GET','POST'])
def rqst():
    s4 = Singleton()
    data = s4.pdData
    if request.method == 'POST':
        requestData = request.get_json(force=True)
        dct, dt = MakeARequest(requestData, data, s4.header)
        s4.requestData = dt
        return dct
    else:
        return GetDictColumns(data, 0)

    
@app.route("/fileSave", methods=['GET','POST'])
def SaveCSV():
    s5 = Singleton()
    data = s5.pdData
    rqs = s5.requestData
    path = ''
    if request.method == 'POST':
        requestData = request.get_json(force=True)
        print(requestData)
        if requestData['saveRequestTable']:
            rqs.to_csv('fileRqst.csv', index=False, header=None)
            path = 'fileRqst.csv'
        if requestData['saveMainTable']:
            data.to_csv('fileMain.csv', index=False, header=None)
            path = 'fileMain.csv'
        return send_file(path, as_attachment=True)
    else:
        return {'Success': 'File is saved'}
    
@app.route("/sandbox", methods=['POST'])
def sndbx():
    s6 = Singleton()
    data = s6.pdData
    if request.method == 'POST':
        requestData = request.get_json(force=True)# тут словарь из строк кода
        lstofStr = list(requestData.values())
        output = mainFunk(s6.filename, lstofStr)
        print('_________________________________')
        print(output)
        print('_________________________________')
        if len(output["user_stderr"]):
            return output["user_stderr"]
        print(output["user_stdout"])
        return output["user_stdout"]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


