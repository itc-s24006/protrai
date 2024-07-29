#s24006
#Flaskを使ったメッセージアプリ
# protrai/flask_msg_rensyu.py
#実際のメッセージを記録するファイルは~protrai/data.txtとする
#


from flask import Flask, render_template,request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/himitsu')
def himitsu():
    return "<small>秘密のページです</small>"

@app.route('/msg')
def msg():
    return render_template('msg.html')

@app.route('/submit', methods=['POST'])
def submit():
    #フォームから入力された内容を取得
    content = request.form['content']
    #data.txtを開いてaの追記モードでデータ追記
    with open('data.txt','a') as file:
        file.write(f"\n{datetime.datetime.now()}\n{content}\n")
        return """
                書き込みましたよ<br>
                <br>
                <br>
                <a href="/msg"><small>もう一度送る</small></a>
                """


if __name__=="__main__":
    app.run(host='0.0.0.0' ,port='5000' ,debug=True)
