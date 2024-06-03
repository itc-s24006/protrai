#GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ

root = tk.Tk() #始めのおまじない

root.geometry("600x400") #ウィンドウのサイズを決める
root.title("ハローアプリ") #ウィンドウのタイトルを決める

ldl = tk.Label(text="こんにちは、世界")#いつもの
ldl2 = tk.Label(text="はじめてのGUI")
ldl.pack() #ldlを配置させる文だよ
ldl2.pack()


root.mainloop() #終わりのおまじない
