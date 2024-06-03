# turtle5.py
#バラを描く


from turtle import * #タートルグラフィックスを使う準備

shape("turtle") #カメの登場

a = 0
while a<200:
    left(70)
    forward(a)
    a = a + 3


done() #おしまい
