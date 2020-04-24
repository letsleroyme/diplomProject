from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
from flask_session import Session
#from werkzeug import secure_filename
from flask import g
app = Flask(__name__)
sess = Session()

@app.route("/", methods=['GET','POST'])
def upload():
    error = None
    if request.method == 'POST':
        f = request.files['fileU']
        file_name = f.filename
        g.data = file_name
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

@app.before_request
def before_request():
    g.field = get_field(NUM)
#https://ru.stackoverflow.com/questions/779534/%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D1%87%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-%D0%B2%D1%8C%D1%8E%D1%88%D0%BA%D0%B0%D0%BC%D0%B8-python-flask
@app.route("/showTable")
def showTable():
    fileName = getattr(g, 'data', None)
    data = pd.read_csv('titanic.csv', header=None)
    print(fileName)
    c = data.count
    names = data.iloc[0, :]
    data = data.iloc[1:, :]
    return render_template('showtable.html', data=data.iloc[0, :], name=names, row=c)


if __name__ == "__main__":
    app.run()


