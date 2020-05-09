from flask import Flask, request, jsonify, redirect, url_for, g
from flask_cors import CORS
import pandas as pd
from Back.ProcessData import *

#from werkzeug import secure_filename
from Back.ProcessData import GetDict

app = Flask(__name__)

CORS(app)

@app.route("/", methods=['GET','POST'])
def upload():
    f = request.files['file']
    fileName = f.filename
    formt = fileName.split(".")
    if formt[1] != 'csv':
        response = jsonify({'status': 415, 'error': 'Unsupported Media Type',
                            'message': 'Wrong type of file'})
        response.status_code = 415
        return response
    f.save('C:\\Users\\Дарья\\Desktop\\Диплом\\diplomProject\\Back\\' + fileName)
    data = pd.read_csv(fileName, header=None)
    g.filename = fileName
    g.dataframe = data
    dct = GetDictFromPandas(data)
    return jsonify(dct)


@app.route("/table", methods=['GET','POST'])
def tbl():
    #filename = getattr(g, 'filename', None)
    #data = getattr(g, 'dataframe', None)
    data = pd.read_csv('titanic.csv', header=None)
    if request.method == 'POST':
        a = request.form.get('action1_check1')
        b = request.form.get('action1_check2')
        c = request.form.get('action2_check1')
        d = request.form.get('action2_check2')
        e = request.form.get('action2_check3')
        f = request.form.get('action3_check1')
        g = request.form.get('action3_check2')
        h = request.form.get('action3_check3')

        if a == False:
            return jsonify({'fail': 'action1_check1 is False'})
        else:
            return jsonify({'success': 'action1_check1 is recieved'})
        #обработка чекбоксов
        #обработка датасета согласно чекбоксам
    else:
        return jsonify(GetDict(data))# вернуть список столбцов в виде джсон


if __name__ == "__main__":
    app.run()


