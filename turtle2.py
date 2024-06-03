# turtle2.py
#カラフルな星を描く

from turtle import * #タートルグラフィックスを使う準備

shape("turtle") #カメの登場
col = ["orange","limegreen","gold","plum","tomato"]

for i in range(5):
    color(col[i])
    forward(200)
    left(144)



done() #おしまい
