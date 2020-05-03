from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import pandas as pd

#from werkzeug import secure_filename
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
    dct = GetDictFromPandas(data)
    return jsonify(dct)


def GetDictFromPandas(data):
    cols = data.shape[1]
    rows = data.shape[0]
    a =[c for c in range(1, cols+1)]
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


if __name__ == "__main__":
    app.run()


