#s24006
#app2.py


import tkinter as tk

def dispLabel():
    lbl1.config(text="こんにちは")

def dispLabel2():
    lbl2.config(text="えらい！！！！")

root = tk.Tk() #画面を作る
root.geometry("400x200") #画面サイズを決める

lbl1 = tk.Label(text="",font=("Helvetica",10)) #ラベルをつくる
btn1 = tk.Button(text="挨拶",command=dispLabel,font=("Helvetica",10)) #ボタンをつくる、dispLabelを呼び出し

lbl2 = tk.Label(text="",font=("Helvetica",30))
btn2 = tk.Button(text="褒める",command=dispLabel2,font=("Helvetica",10)) 

lbl1.pack() #画面にラベルを配置
btn1.pack() #画面にボタンを配置
lbl2.pack()
btn2.pack()
tk.mainloop() #作ったウィンドウを表示する
