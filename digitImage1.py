#s24006
#数値データをグレーの濃淡画像にするプログラム

import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[5],cmap="Greys") #数値データをグレーの濃淡画像にする
plt.show() #作った画像を表示する
