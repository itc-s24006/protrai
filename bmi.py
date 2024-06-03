#s24006
#BMI値計算プログラム

h = float(input("身長を入力してください。:"))/ 100.0
w = float(input("体重を入力してください。:"))

bmi = w /(h * h)
print("あなたのBMI値は",bmi,"です。")
