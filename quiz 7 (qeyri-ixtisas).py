#Tapsirig 1 Matrisdə "Güzgü" Analizi
'''
def maxi(a):
    maxx = float('-inf')
    for i in a:
        if i > maxx:
            maxx = i
    return maxx
def mini(a):
    minn = float('inf')
    for i in a:
        if i < minn:
            minn = i
    return minn
from random import randint
n = int(input('N-i daxil edin: '))
a = [[randint(10, 99) for i in range(n)] for i in range(n)]
for i in range(n):
    print(f'Setir {i}:', end = '')
    for j in range(n):
        print(f'{a[i][j]:10d}', end = '')
    print()
print()
print('Tehlil (0-dan baslayaraq):')
print('1. Tek nomreli sutunlar ( ', end = '')
for j in range(n):
    if j % 2 == 1:
        print(f'Sutun {j}', end = ' ')
print(')')
sutun_maxi = []
for j in range(n):
    sutun = []
    if j % 2 == 1:
        print(f'    Sutun {j}:', end = ' ')
        for i in range(n):
            sutun += [a[i][j]]
        print(f'{sutun} -> Max: {maxi(sutun)}')
        sutun_maxi += [maxi(sutun)]
eded1 = maxi(sutun_maxi)
print(f'    >> Bu qrupda en boyuk (Max): {eded1}')
print()
print('2. Cut nomreli setirler ( ', end = '')
for i in range(n):
    if i % 2 == 0:
        print(f'Setir {i}', end = ' ')
print(')')
setir_mini = []
for i in range(n):
    if i % 2 == 0:
        print(f'    Setir {i}: {a[i]} -> Min: {mini(a[i])}')
        setir_mini += [mini(a[i])]
eded2 = mini(setir_mini)
print(f'    >> Bu qrupda en kicik (Min): {eded2}')
print()
print(f'Netice ({eded1} + {eded2}) // 2: {(eded1 + eded2) // 2}')
'''

#Tapsirig 2 "Unikal Qonşular"ın Tapılması
'''
def sayan(a):
    for i in a:
        say = 0
        for k in a:
            if i == k:
                say += 1
        if say == 1:
            return i
def boleni(a):
    for i in range(1, a):
        if a % i == 0:
            bolen = i
    return bolen
x = map(int, input('Siyahi elemenlerini daxil edin (bosluqla): ').split())
listt = []
for i in x:
    listt += [i]
print()
print(f'Daxil edilmis siyahi: {listt}')
print()
unikal = sayan(listt)
print('Tehlil:')
print(f'1. Ilk tekrarlanmayan (unikal) eded: {unikal}')
print(f'2. {unikal}-nin ozunden basqa en boyuk boleni: {boleni(unikal)}')
print()
print(f'Netice: {boleni(unikal)}')
'''

#Tapsirig 3 "Simvol Sıxılma" Redaktoru
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
def sayan(a, b):
    say = 0
    for i in a:
        if i == b:
            say += 1
    return say
text = input('Metni daxil edin: ') + ' '
print()
print(f'Daxil edilmis metn: {text}')
print()
print('Tehlil:')
print('1. Ardicil simvollarin sixilmasi: ', end = '')
i = 0
yekun = ''
while i < uzun(text) - 1:
    if ('a' <= text[i] <= 'z' or 'A' <= text[i] <= 'Z') and text[i] == text[i + 1]:
        yekun += text[i] + str(sayan(text, text[i]))
        i += sayan(text, text[i])
    else:
        i += 1
print(yekun)
print('2. Reqemin kodlasdirilmasi: ', end ='')
for i in text:
    if '0' <= i <= '9':
        print(f'{i} -> ({i})', end = ' ')
print()
print('3. Bosluqlarin deyisdirilmesi: " " -> "-"')
print()
yekun = ''
i = 0
while i < uzun(text) - 1:
    if '0' <= text[i] <= '9':
        yekun += '(' + text[i] + ')'
        i += 1
    elif text[i] == ' ':
        yekun += '-'
        i += 1
    elif ('a' <= text[i] <= 'z' or 'A' <= text[i] <= 'Z') and text[i] == text[i + 1]:
        yekun += text[i] + str(sayan(text, text[i]))
        i += sayan(text, text[i])
    else:
        yekun += text[i]
        i += 1
print(f'Netice: {yekun}')
'''

#Tapsirig 4 Rəqəmsal "Xalis Sərvət" Hesablanması
'''
def tekreqemler(a):
    tek = []
    while a:
        if (a % 10) % 2 == 1:
            tek += [a % 10]
        a //= 10
    return tek[-1::-1]
def cutreqemler(a):
    cut = []
    while a:
        if (a % 10) % 2 == 0:
            cut += [a % 10]
        a //= 10
    return cut[-1::-1]
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
x = int(input('Natural eded daxil edin: '))
print()
print(f'Daxil edilmis eded: {x}')
print()
print('Tehlil:')
print('1. Tek reqemlerin hasili (', end = '')
tekler = tekreqemler(x)
hasil = 1
for i in range(uzun(tekler)):
    hasil *= tekler[i]
    if i != uzun(tekler) - 1:
        print(f'{tekler[i]}', end = ' * ')
    else:
        print(f'{tekler[i]}): {hasil}')
print('2. Cut reqemlerin cemi (', end = '')
cutler = cutreqemler(x)
cem = 0
for i in range(uzun(cutler)):
    cem += cutler[i]
    if i != uzun(cutler) - 1:
        print(f'{cutler[i]}', end = ' + ')
    else:
        print(f'{cutler[i]}): {cem}')
print('3. Muqayise: ', end = '')
if hasil > cem:
    flag = -1
    print(f'{hasil} > {cem} (Hasil Cemden boyukdur)')
else:
    if cem > hasil:
        print(f'{hasil} < {cem} (Cem Hasilden boyukdur)')
        flag = 0
    else:
        print(f'{hasil} = {cem}')
print()
print(f'Netice: ', end = '')
if flag == -1:
    print('Aktiv Eded')
elif flag == 0:
    print('Passiv Eded')
'''

#Tapsirig 5 Sözlərin "Gücünə" görə Sıralanması
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
def sait(a):
    saitler = 'aeuio'
    b_saitler = 'AEUIO'
    saitsay = 0
    samitsay = 0
    for i in a:
        if i in saitler or i in b_saitler:
            saitsay += 1
        else:
            samitsay += 1
    return saitsay, samitsay
def bubble(a):
    n = uzun(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sait(a[j])[1] > sait(a[j + 1])[1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            elif sait(a[j])[1] == sait(a[j + 1])[1]:
                if sait(a[j])[0] > sait(a[j + 1])[0]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    return a
cumle = input('Cumleni daxil edin: ') + ' '
print()
print(f'Daxil edilmis cumle: {cumle}')
soz = ''
sozler = []
for i in cumle:
    if i != ' ':
        soz += i
    else:
        if uzun(soz) != 0:
            sozler += [soz]
        soz = ''
print()
print('--- Siralama Prosesi ---')
k = 1
for i in sozler:
    print(f"{k}. '{i}' \t -> {sait(i)[1]} samit, {sait(i)[0]} sait")
    k += 1
print()
print(f'Yekun siralama: {bubble(sozler)}')
'''
