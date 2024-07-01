#s24006
#エントリーウィジェットで受け付けた金額を税込み価格として出力するプログラム


import tkinter as tk

def dispLabel():
    #entryメソッドを利用して入力を受け付け
    a = entry.get()
    print(type(a))
    lbl2.config(text=f"税込み金額は{a}円です。")


root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200")

lbl1 = tk.Label(text="税抜き金額を入力してください。",font=("Helvetica",18))
lbl2 = tk.Label(text=" ",font=("Helvetica",20))
entry = tk.Entry(font=("Helvetica",20))
btn = tk.Button(text="計算",font=("Helvetica",20),command=dispLabel)

lbl1.pack()
entry.pack()
btn.pack()
lbl2.pack()
tk.mainloop()
