#s24006
#時間を表示させる「時計アプリ」を作成
#モジュール名「time_kadai.py」
#時計アプリを使いやすいようにバージョンアップする

import datetime
import tkinter as tk #GUIでアプリを作ることができるモジュール

#時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日　%H時%M分%S秒")
    
    lbl.config(text=current_time) #アプリ(ウィンドウ)に中身を挿入
    root.after(1000,update_time)

#Tkinterのウィンドウを作成
root = tk.Tk()

root.title("⌚時計アプリ⌚")

lbl = tk.Label()
lbl.config(text="",font=("Helvetica",15))
lbl.pack()

#関数の呼び出し
update_time()

root.mainloop()
