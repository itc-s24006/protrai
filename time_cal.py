#s24006
#現在の時刻と2024/06のカレンダーを表示するプログラム


import calendar as cal
import datetime as dt

print(cal.month(2024,6))
now = dt.datetime.now()
print(now.strftime("%Y年%m月%d日 %H:%M:%S"))
