from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import pandas as pd
import json
from Back.ProcessData import *

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

@app.route("/", methods=['GET','POST'])
def upload():
    f = request.files['file']
    fileName = f.filename
    fort = fileName.split(".")
    if fort[1] != 'csv':
        response = jsonify({'status': 415, 'error': 'Unsupported Media Type',
                            'message': 'Wrong type of file'})
        response.status_code = 415
        return response
    f.save('C:\\Users\\Дарья\\Desktop\\Диплом\\diplomProject\\Back\\' + fileName)
    data = pd.read_csv(fileName, header=None)

    dct = GetDictFromPandas(data)
    return jsonify(dct)


@app.route("/table", methods=['GET','POST'])
def tbl():
    data = pd.read_csv('titanic.csv', header=None)
    #data = data.iloc[1:, :]
    #outdata= data.copy()
    if request.method == 'POST':
        requestDict = request.get_json(force=True)
        '''if requestDict['action1_check1']:
            outdata = ReplaceNanForNumeric(outdata, 6, 'titanic.csv')

        if requestDict['action1_check2'] or requestDict['action2_check2'] or requestDict['action3_check3']:
            outdata = RemoveNanForCol(outdata, 11)

        if requestDict['action2_check1']:
            outdata = ReplaceNanForCategoric(outdata, 12)

        if requestDict['action2_check3']:
            outdata = ReplaceTextCategToNum(outdata, 12)

        if requestDict['action3_check1']:
            outdata = GetLowLetterForText(outdata, 4)

        if requestDict['action3_check2']:
            outdata = GetTextWithoutDots(outdata, 4)'''

        if requestDict['action1_check1']:
            return jsonify({'success':'action1_check1 is True'})
    else:
        return jsonify(GetDict(data))# вернуть список столбцов в виде джсон


if __name__ == "__main__":
    app.run(debug=True)


