from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
#from werkzeug import secure_filename
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def upload():
    error = None
    if request.method == 'POST':
        f = request.files['fileU']
        file_name = f.filename
        f.save('C:\\Users\\Дарья\\Desktop\\Диплом\\diplomProject\\Back\\' + file_name)
        return redirect(url_for('showTable', error=error, file=file_name))
    # else:
    #     return "Ошибка"
    return render_template('upload.html', error=error)
    
@app.route("/uploadSucc", methods=['GET','POST'])
def uploadSucc():
    if request.method == 'POST':
        return "Успешно."
    return "Успешно."

def GetDictFromPandas(data):
    cols = data.shape[1]
    rows = data.shape[0]
    print(cols)
    d = {}
    for i in range(rows):
        lst = []
        for j in range(cols):
            lst.append(data.iloc[i, j])
        d[i] = lst
    return d


@app.route("/showTable")
def showTable():
    fileName = request.args.get('file')
    #data = pd.read_csv('data-logistic.csv', header=None)
    data = pd.read_csv(fileName, header=None)
    dct = GetDictFromPandas(data)
    return render_template('showtable.html', data=dct)


if __name__ == "__main__":
    app.run()


