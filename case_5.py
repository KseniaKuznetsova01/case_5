"""Case-study #5 Парсинг web-страниц
Developers:
Panyukova E.
Kuznetsova K.

"""
file_out = open('output.txt', 'w')                                      # Create  file output.txt of delete text in it
file_out.close()
import urllib.request
with open('input.txt') as inp_file:                                     # Open file input.txt and use link
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
        total_2 = new_total
        zap = total_2.find(',')                                         # Change commas for float
        while zap != -1:
            total_2 = total_2[:zap] + '.' + total_2[zap + 1:]
            zap = total_2.find(',')
        prob = total_2.find(' ')                                        # Found values using spaced
        comp = float(total_2[:prob])
        total_2 = total_2[prob + 1:]
        prob = total_2.find(' ')

        att = float(total_2[:prob])
        total_2 = total_2[prob + 1:]
        prob = total_2.find(' ')

        pct = total_2[:prob]
        total_2 = total_2[prob + 1:]
        prob = total_2.find(' ')

        yds = float(total_2[:prob])
        total_2 = total_2[prob + 1:]
        prob = total_2.find(' ')

        avg = total_2[:prob]
        total_2 = total_2[prob + 1:]
        prob = total_2.find(' ')

        td = float(total_2[:prob])
        total_2 = total_2[prob + 1:]
        prob = total_2.find(' ')
        tni = float(total_2[:prob])

        if comp % 1 == 0:                                            # Change float to int
            comp = int(comp // 1)
        if att % 1 == 0:
            att = int(att // 1)
        if yds % 1 == 0:
            yds = int(yds // 1)
        if td % 1 == 0:
            td = int(td // 1)
        if tni % 1 == 0:
            tni = int(tni // 1)
        a = (comp / att - 0.3) * 5
        b = (yds / att - 3) * 0.25
        c = (td / att) * 20
        d = 2.375 - (tni / att * 25)
        ps = (a + b + c + d) / 6 * 100
        ps = '{0:<7.0f}'.format(ps)

        if comp % 1 == 0:                                          # Round off
            comp = int(comp // 1)
            comp = '{0:<7.0f}'.format(comp)
        else:
            comp = '{0:<7.2f}'.format(comp)
        if att % 1 == 0:
            att = int(att // 1)
            att = '{0:<7.0f}'.format(att)
        else:
            att = '{0:<7.2f}'.format(att)
        if yds % 1 == 0:
            yds = int(yds // 1)
            yds = '{0:<7.0f}'.format(yds)
        else:
            yds = '{0:<7.2f}'.format(yds)
        if td % 1 == 0:
            td = int(td // 1)
            td = '{0:<7.0f}'.format(td)
        else:
            td = '{0:<7.2f}'.format(td)
        if tni % 1 == 0:
            tni = int(tni // 1)
            tni = '{0:<7.0f}'.format(tni)
        else:
            tni = '{0:<7.2f}'.format(tni)

        file_out = open('output.txt', 'a')                       # Save to file output.txt
        print(name.ljust(20), comp, att, yds, td, tni, ps, file=file_out)
        file_out.close()

