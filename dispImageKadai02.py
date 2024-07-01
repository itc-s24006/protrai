#s24006
#dispImageにグレースケール、９０度回転、水平反転機能追加
#dispImageKadai.py

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読み込んで、モザイクに変換
    newImage = PIL.Image.open(path).convert("L").rotate(90) \
               .transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300,300))
    #そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl2 = tk.Label(text=fpath,font=("Helbetica",10))
        lbl2.pack()

root = tk.Tk()
root.geometry("400x400")

lbl = tk.Label(text="画像表示アプリ バージョン2.0",font=("Helbetica",8))
btn = tk.Button(text="ファイルを開く",command = openFile)
imageLabel = tk.Label()
lbl.pack()
btn.pack()
imageLabel.pack()


tk.mainloop()
