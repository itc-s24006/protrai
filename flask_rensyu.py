#s24006
#Flaskの練習

from flask import Flask  #事前にflask外部モジュールをインストールすると使える

'''Flaskライブラリをインスタンス化し、app変数に割り当て
その際、コンストラクタへの引数は実行中のモジュールを指定する
'''
app = Flask(__name__)

'''ルートＵＲＬに対するリクエストを処理する関数を定義するデコレーター
引数に'/'を指定するとアクセスした際index()関数が呼び出される
'''
@app.route('/')
def index():
    return "<h1>Hello world.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    
