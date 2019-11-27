"""Case-study #5 Парсинг web-страниц
Developers:
Panyukova E.
Kuznetsova K.

"""
import urllib.request
with open('input.txt') as inp_file:
    for line in inp_file.readlines():
        url = line
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
        count = 1
        while i != -1:
            num = str(total[m + 4: i])
            new_total += num + ' '
            total = total[i + 1:]
            i = total.find('</td>')
            m = total.find('<td>')
        total_2 = new_total[:28]

        probel = total_2.find(' ')
        comp = float(total_2[:probel])
        total_2 = total_2[probel + 1:]
        probel = total_2.find(' ')
        att = float(total_2[:probel])
        total_2 = total_2[probel + 1:]
        probel = total_2.find(' ')
        pct = total_2[:probel]
        total_2 = total_2[probel + 1:]
        probel = total_2.find(' ')
        yds = float(total_2[:probel])
        total_2 = total_2[probel + 1:]
        probel = total_2.find(' ')
        avg = total_2[:probel]
        total_2 = total_2[probel + 1:]
        probel = total_2.find(' ')
        td = float(total_2[:probel])
        total_2 = total_2[probel + 1:]
        probel = total_2.find(' ')
        tni = float(total_2[:probel])
        print(name, new_total[:30])



