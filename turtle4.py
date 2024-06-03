# turtle4.py
#カラフルな花を描く

from turtle import * #タートルグラフィックスを使う準備

shape("turtle") #カメの登場
#col = ["orange","limegreen","gold","plum","tomato"]
col = ["red","blue","green","brown","black"]

for i in range(5):
    color(col[i]) #半径１００の円を描くこと
    circle(100)
    left(72)



done() #おしまい
