import tkinter as tk

root = tk.Tk() #画面を作る
root.geometry("200x100") #画面サイズを決める

lbl = tk.Label(text="LABEL") #ラベルをつくる
btn = tk.Button(text="PUSH") #ボタンをつくる

lbl.pack() #画面にラベルを配置
btn.pack() #画面にボタンを配置
tk.mainloop()
