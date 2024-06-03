#s24006
#GUIで動作するおみくじ

import tkinter as tk
import random

root = tk.Tk()

root.geometry("300x300")
root.title("GUIおみくじ")

kuji = ["大吉","中吉","小吉","凶"]
ldl = tk.Label(text=random.choice(kuji))
ldl.pack()


root.mainloop()
