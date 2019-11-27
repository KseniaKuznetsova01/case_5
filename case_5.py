"""Case-study #5 Парсинг web-страниц
Developers:
Panyukova E.
Kuznetsova K.

"""
import urllib.request
url = 'http://www.nfl.com/player/brycepetty/2552369/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find('player-name')
name = text[text.find('>', part_name)+1:text.find('&', part_name)]
part_total = text.find('TOTAL')
total = text[text.find('>', part_total) + 1:text.find('</tr>', part_total)]
new_total = ''
i = total.find('</td>')
m = total.find('<td>')
while i != -1:
    num = total[m + 4: i]
    new_total += num + ' '
    total = total[i + 1:]
    i = total.find('</td>')
    m = total.find('<td>')


print(new_total)
print(name)
