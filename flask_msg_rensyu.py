#s24006
#Flaskを使ったメッセージアプリ
# protrai/flask_msg_rensyu.py
#実際のメッセージを記録するファイルは~protrai/data.txtとする
#


from flask import Flask, render_template,request
import datetime

app = Flask(__name__)

#ルート/にアクセスすると、index.htmlテンプレートがレンダリングされる
@app.route('/')
def index():
    return render_template('index.html')

#ルート/himitsuにアクセスすると、「秘密のページです」というテキストが表示される
@app.route('/himitsu')
def himitsu():
    return "<small>秘密のページです</small>"

#ルート/msgにアクセスすると、msg.htmlテンプレートがレンダリングされる
@app.route('/msg')
def msg():
    return render_template('msg.html')

"""
ルート/submitはPOSTリクエストを受け付ける。
通常、HTMLフォームの送信先として使用される
書き込みが完了したら「書き込みましたよ」というメッセージを返す
"""
@app.route('/submit', methods=['POST'])
def submit():
    #フォームから送信されたデータ(content)を取得
    content = request.form['content']
    #data.txtファイルを追記モードで開き、現在の日時とともにcontentの内容をファイルに書き込む
    with open('data.txt','a') as file:
        file.write(f"\n{datetime.datetime.now()}\n{content}\n")
        return """
                書き込みましたよ<br>
                <br>
                <br>
                <a href="/msg"><small>もう一度送る</small></a>
                """

#スクリプトが直接実行された場合、Flaskアプリケーションをローカルホストのポート5000でデバッグモードで起動する
if __name__=="__main__":
    app.run(host='0.0.0.0' ,port='5000' ,debug=True)
