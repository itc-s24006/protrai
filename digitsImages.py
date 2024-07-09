#s24006
#手書き数字を読み込んで判断するプログラム

import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

#画像ファイルを数値リストに変換する
def imageToData (filename):
    grayImage = PIL.Image.open (filename) .convert ("L")
    grayImage = grayImage.resize ( (8, 8), PIL.Image.Resampling.LANCZOS)
    numImage = numpy.asarray (grayImage, dtype = float)
    numImage = 16-numpy.floor (17*numImage/256)
    numImage = numImage.flatten()
    print(numImage)
    return numImage

#数値を予測する
def predictDigits (data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC (gamma=0.001)
    clf.fit (digits.data,digits.target)
    n = clf.predict ([data])
    print("予測=",n)
data = imageToData ("tmp/2.png")#パスを確認する
predictDigits (data)
