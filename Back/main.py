from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

#from werkzeug import secure_filename
app = Flask(__name__)

CORS(app)

@app.route("/", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        fileName = f.filename
        f.save('C:\\Users\\Дарья\\Desktop\\Диплом\\diplomProject\\Back\\' + fileName)
        data = pd.read_csv(fileName, header=None)
        dct = GetDictFromPandas(data)
        return jsonify(dct)

def GetDictFromPandas(data):
    cols = data.shape[1]
    rows = data.shape[0]
    d = {}
    for i in range(rows):
        lst = []
        for j in range(cols):
            lst.append(data.iloc[i, j])
        d[i] = lst
    return d


if __name__ == "__main__":
    app.run()


