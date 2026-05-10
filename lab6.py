#1 Klaviaturadan daxil edilən simvolun həmin mətnin içində mövcud olub-olmadığını yoxlayan proqram
'''setir = input('Setri daxil edin: ')
yekun = []
x = input('Axtarilir: ')
for i in range(len(setir)):
    yekun += setir[i]
if x in yekun:
    print('Vardir.')
else:
    print('Yoxdur.')'''

#2 Klaviaturadan simvollar sətri daxil edin və onda olan bütün «a» hərflərini «b» hərfi ilə və «b» hərflərini «a» hərfi ilə əvəz eden proqram
'''setir = input('Setri daxil edin: ')
yekun = []
son = ''
for i in range(len(setir)):
    yekun += setir[i]
for i in range(len(yekun)):
    if yekun[i] == 'a':
        yekun[i] = 'b'
    elif yekun[i] == 'b':
        yekun[i] = 'a'
    elif yekun[i] == 'B':
        yekun[i] = 'A'
    elif yekun[i] == 'A':
        yekun[i] = 'B'
    son += yekun[i]
print(son)'''

#3 Simvollu sətri daxil edib və həmin sətirdə olan sözlərin sayını tapan funksiya 
'''setir = ' ' + input('Setri daxil edin: ') + ' '  
soz = ''
sozler = []
for i in range(len(setir)):
    if 'a' <= setir[i] <= 'z' or 'A' <= setir[i] <= 'Z':
        soz += setir[i]
    else:
        if len(soz) != 0:
            sozler += [soz]
        soz = ''
print(f' Tapilmis sozlerin sayi: {len(sozler)}')'''

#4 Simvollu sətri daxil edin və həmin sətirdə olan ən uzun sözü (və onun uzunluğunu) tapan proqram
'''def uzun(a):
    say = 0
    yeni = ''
    for i in range(len(a)):
        yeni += a[i]
        say += 1
    return say
setir = ' ' + input('Setri daxil edin: ') + ' '  
soz = ''
sozler = []
for i in range(len(setir)):
    if 'a' <= setir[i] <= 'z' or 'A' <= setir[i] <= 'Z':
        soz += setir[i]
    else:
        if len(soz) != 0:
            sozler += [soz]
        soz = ''
maxx = float('-inf')
for i in sozler:
    if uzun(i) > maxx:
        uzunsoz = i
        maxx = uzun(i)
print(f' En uzun soz: {uzunsoz}, uzunlugu {maxx}')'''

#5 Ekrana soyadınız və inisiallar çixaran proqram
'''a = input('Soyad, ad və ata adınızı daxil edin: ') + ' '
soz = ''
sozler = []
for i in range(len(a)):
    if 'a' <= a[i] <= 'z' or 'A' <= a[i]:
        soz += a[i]
    else:
        if len(soz) != 0:
            sozler += [soz]
        soz = ''
print(f' Netice: {sozler[1][0]}.{sozler[2][0]}. {sozler[0]}')'''

#6 Faylın ünvanını daxil edin və «/» işarəsi ilə ayrılmış hissələrə bölen proqram
'''unvan = input('Faylin unvanini daxil edin: ') + ' '
unvann = ''
xususisareler = '.,:?!@1234567890-'
for i in range(len(unvan)):
    if 'a' <= unvan[i] <= 'z' or 'A' <= unvan[i] <= 'Z' or unvan[i] in xususisareler:
        unvann += unvan[i]
    else:
        if len(unvann) != 0:
            print(unvann)
        unvann = '''''

#7 Sətirdə bir simvollar ardıcıllığını digər ardıcıllıq ilə əvəzləyən proqram
'''def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
setir = input('Setri daxil edin: ')
evezedir = input('Neyi evezleyirik: ')
neile = input('Ne ile evezleyirik: ')
yekun = ''
i = 0
for i in range(uzun(setir)):
    if setir[i:i + uzun(evezedir)] == evezedir:
       yekun += neile
       i += uzun(evezedir)
    else:
        yekun += setir[i]
print(yekun)'''

#8 Daxil edilmiş cümlədə axtarılan simvolların sayını müəyyən eden proqram
'''def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
setir = input('Input: ')
axtar = input('Axtarilan soz: ')
count = 0
for i in range(uzun(setir)):
    if setir[i:i + uzun(axtar)] == axtar:
        count += 1
        i += uzun(axtar)
print(f'{axtar} simvollarinin sayi: {count}')'''

#9 Daxil edilmiş cümlədə axtarılan simvolların sayını müəyyən eden ve deyisen proqram
'''def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
setir = 'Bayram günü gələcəyik sizə bayramlaşmağa. Bayramlaşsaz da bayramlaşacağıq. Bayramlaşmasanız da bayramlaşacağıq.'
count = 0
yekun = ''
i = 0
while i < uzun(setir):
    if setir[i:i + 6] == 'bayram':
        count += 1
        yekun += 'novruz'
        i += 6
    elif setir[i:i + 6] == 'Bayram':
        count += 1
        yekun += 'Novruz'
        i += 6
    else:
        yekun += setir[i]
        i += 1
print(yekun)'''

#10 Daxil edilmiş cümlədə axtarılan simvolların sayını müəyyən eden ve deyisen proqram
'''def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
setir = 'Haqqı, haqqıya getmiş, Haqqı, haqqıdan haqqını istəmiş, Haqqı, Haqqının haqqını verməyincə, Haqqı da Haqqının haqqından gəlmiş.'
count = 0
yekun = ''
i = 0
while i < uzun(setir):
    if setir[i:i + 5] == 'haqqı':
        count += 1
        yekun += 'sarı'
        i += 5
    elif setir[i:i + 5] == 'Haqqı':
        count += 1
        yekun += 'Sarı'
        i += 5
    else:
        yekun += setir[i]
        i += 1
print(yekun)'''

#11 Daxil edilmiş cümlədə sözlərin 2-ci hərfini silib yeni cümlədə yazan proqram
'''def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
setir = input('Input: ') + ' '
soz = ''
sozler = []
yekun = ''
isareler = '1234567890,.!@#$%^&*()_+-='
for i in range(len(setir)):
    if 'a' <= setir[i] <= 'z' or 'A' <= setir[i] <= 'Z' or setir[i] in isareler:
        soz += setir[i]
    else:
        if len(soz) != 0:
            sozler += [soz]
            sozler += ' '
        soz = ''
for j in sozler:
    for k in range(len(j)):
        if k != 1:
            yekun += j[k]
print(yekun)'''

#12 Klaviaturadan mətn daxil edilir. Həmin mətnin içində aşağıdakı əlifbadan simvollar olub olmadığını yoxlayan proqram
'''def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
setir = input('Setir: ')
sait = 'AOUE'
samit = 'bcmf'
reqem = '3579'
durgu = '!?,;'
yekun = []
for i in range(uzun(setir)):
    if setir[i] in sait and setir[i] not in yekun:
        yekun += setir[i]
for i in range(uzun(setir)):
    if setir[i] in samit and setir[i] not in yekun:
        yekun += setir[i]
for i in range(uzun(setir)):
    if setir[i] in reqem and setir[i] not in yekun:
        yekun += setir[i]
for i in range(uzun(setir)):
    if setir[i] in durgu and setir[i] not in yekun:
        yekun += setir[i]
for i in yekun:
    print(f"'{i}'", end = ' ')
print('simvollari var')'''

#13
'''print('İfadeni daxil edin:')
ifade = input() + '+'
cavab = 0
eded = ''
ededler = []
for i in range(len(ifade)):
    if ifade[i] != '+':
        eded += ifade[i]
    else:
        if len(eded) != 0:
            ededler += [eded]
        eded = ''
print(ededler)
for i in ededler:
    cavab += int(i)
print(f'Cavab: {cavab}')'''

#14
'''ifade = input('İfadeni daxil edin: ') + '+'
eded = ''
ededler = []
operation = []
for i in range(len(ifade)):
    if ifade[i] != '+' and ifade[i] != '-':
        eded += ifade[i]
    else:
        if len(eded) != 0:
            ededler += [eded]
        eded = ''
    if ifade[i] == '+' or ifade[i] == '-':
        operation += ifade[i]
cavab = int(ededler[0])
for i in range(len(operation)):
    if i == 2:
        break
    if operation[i] == '-':
        cavab -= int(ededler[i + 1])
    else:
        cavab += int(ededler[i + 1])
print(cavab)'''

#15
'''setir = input('Sətri daxil edin: ')+ ' '
soz = ''
sozler = []
for i in range(len(setir)):
    if setir[i] != ' ':
        soz += setir[i]
    else:
        if len(soz) != 0:
            sozler += [soz]
        soz = ''
birinci = sozler[0]
print(f'Birinci soz: {birinci}')'''
        
#16
'''file = input('Faylın adını daxil edin: ')
uzanti = input('Faylın yeni genişlənməsini daxil edin: ')
yeni = ''
yeniler = []
if '.' not in file:
    netice = file + '.' + uzanti
else:
    for i in range(len(file)):
        if file[i] != '.':
            yeni += file[i]
        else:
            if len(yeni) != 0:
                yeniler += [yeni]
            yeni = ''
    netice = ''
    for i in yeniler:
        netice += i + '.'
    netice += uzanti
print(netice)'''

#17
'''def uzun(a):
    say = 0
    for i in a:
        say += 1
    return say
file = input('Fayla daxil edilecek adi yazin: ')
olmaz = '/:*?"<>|\'
if olmaz in file or uzun(file) > 10:
    print('Xeta')
else:
    print(f'{file} adi excel fayli ucun ugurludur.')'''

#18
'''file = input('Qovluq adi daxil edin >> ')
letter = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
specials = '.-_~=:'
def cons(file):
    flag = 0
    if not(5 <= len(file) <= 15):
        return '5<=Simvol sayı>= 15 olmalıdır!'
    for i in file:
        if i not in (letter + uppercase + digits + specials):
            return 'Qovluq adinda yalniz kicik, boyuk herf, reqem ve xususi simvol olmalidir(.-~_=:)'
    for i in file:
        if i in letter:
            flag += 1
            break
    if flag == 0:
        return 'Yanlış! Ən az 1 kicik herf olmalıdır!'
    for i in file:
        if i in uppercase:
            flag += 1
            break
    if flag == 1:
        return 'Yanlış! Ən az 1 boyuk herf olmalıdır!'    
    for i in file:
        if i in digits:
            flag += 1
            break
    if flag == 2:
        return 'Yanlış! Ən az 1 reqem olmalıdır!'
    for i in file:
        if i in specials:
            flag += 1
            break
    if flag == 3:
        return 'Yanlış! Ən az 1 xususi simvol olmalıdır!'
    return 'Duzgun qovluq adi!'
print(cons(file))'''
