#s24006
#「沖縄県の推計人口」のページからデータを抽出するプログラム

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

html.encoding = 'Shift_JIS'


soup = BeautifulSoup(html.text, 'html.parser')
#タイトル出力
print(soup.find("title").string)
#人口出力
table = soup.find('table', class_='table1 font2 gyo5')

a = []
#表示形式に編集
a.append(soup.find_all('td align="right"','td align="center"'))
print(a)
#for element in suikei.find_all('td','td align="right"','td align="center"'):
    #print(element['td','td align="right"','td align="center"'])

