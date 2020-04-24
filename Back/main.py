from flask import Flask, render_template, redirect, url_for, request
#from werkzeug import secure_filename
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def upload():
    error = None
    if request.method == 'POST':
        f = request.files['fileU']
        file_name = f.filename
        f.save('C:\\Users\\Дарья\\Desktop\\Диплом\\diplomProject\\Back' + file_name)
        return redirect(url_for('uploadSucc', error=error))
    # else:
    #     return "Ошибка"
    return render_template('upload.html', error=error)
    
@app.route("/uploadSucc", methods=['GET','POST'])
def uploadSucc():
    if request.method == 'POST':
        return "Успешно"
    return "Успешно."




if __name__ == "__main__":
    app.run()