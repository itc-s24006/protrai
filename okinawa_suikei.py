#s24006
#「沖縄県の推計人口」のページからデータを抽出するプログラム

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

#文字コードをshift_JISにエンコーディング
html.encoding = 'Shift_JIS'


soup = BeautifulSoup(html.text, 'html.parser')
#タイトル出力
print(soup.find("title").string)
#人口出力
table = soup.find('table', class_='table1 font2 gyo5')

a = []
#tableからtdタグの「align="right"」のものだけをaリストに追加する
for element in table.find_all('td',align="right"):
    a.append(element.text)

print(f"総人口：{a[0]}")
print(f"男：{a[1]}")
print(f"女：{a[2]}")



    #print(element['td','td align="right"','td align="center"'])

