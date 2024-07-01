#s24006
#omikujiApp.py


import random
import tkinter as tk


kuji = ["大吉","中吉","小吉","凶","大凶","半吉","末吉","大大吉"]
#print(random.choice(kuji))

def dispLabel():
    lbl.config(text=random.choice(kuji))

root = tk.Tk()
root.geometry("400x200")

lbl = tk.Label(text="",font=("Helvetica",10)) 
btn = tk.Button(text="くじを引く",command=dispLabel,font=("Helvetica",10))

lbl.pack()
btn.pack()
tk.mainloop() 
