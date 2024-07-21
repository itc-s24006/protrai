#s24006
#「こんにちは世界」と書かれたHTML文書を表示するプログラム


'''事前にflask外部モジュールをインストールすると使える
   render_templateはHTMLファイルを扱う際必要
'''
from flask import Flask,render_template  

'''Flaskライブラリをインスタンス化し、app変数に割り当て
その際、コンストラクタへの引数は実行中のモジュールを指定する
'''
app = Flask(__name__)

'''ルートＵＲＬに対するリクエストを処理する関数を定義するデコレーター
引数に'/'を指定するとアクセスした際index()関数が呼び出される
'''
@app.route('/')
def index():
    #templates/index.htmlをあらかじめ作成しておく
    return render_template('index.html')

@app.route('/himitsu')
def index2():
    return render_template('himitsu.html')

if __name__ == '__main__':
    #それぞれのユニークなIPアドレスでアクセスするように設定
    app.run(host='0.0.0.0',port=5000,debug=True)
    
#python flask_rensyu2.pyで実行し、ブラウザから表示させてみましょう
