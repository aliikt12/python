#Tapsirig 1 Sərhəd və Diaqonal Harmoniyası
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
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
n = int(input('N-i daxil edin: '))
matris = []
for i in range(1, n + 1):
    row = []
    x = map(int, input(f'{i}-ci setir elementlerini bosluqla daxil edin: ').split())
    for i in x:
        row += [i]
    matris += [row]
print()
matris2 = []
for j in range(n):
    col = []
    for i in range(n):
        col += [matris[i][j]]
    matris2 += [col]
kenar_maxlar = []
for i in range(n):
    if i == 0 or i == n - 1:
        kenar_maxlar += [maxi(matris[i])]
for j in range(n):
    if j == 0 or j == n - 1:
        kenar_maxlar += [maxi(matris2[j])]
number1 = maxi(kenar_maxlar)
print(f'Kenar elementlerin max-i: {maxi(kenar_maxlar)}')
diaqonal = []
for i in range(n):
    diaqonal += [matris[i][i]]
    diaqonal += [matris[i][n - 1 - i]]
number2 = mini(diaqonal)
print(f'Diaqonallarin min-i: {mini(diaqonal)}')
print(f'Yekun cem: {number1 + number2}')
'''

#Tapsirig 2 İki Liderin Ortaq Gücü
'''
def maxi(a):
    maxx = float('-inf')
    for i in a:
        if i > maxx:
            maxx = i
    return maxx
def second_maxi(a):
    maxx = float('-inf')
    for i in a:
        if i > maxx and i != maxi(a):
            maxx = i
    return maxx
def ebob_tap(a, b):
    if a > b:
        minn = b
    else:
        if a < b:
            minn = a
    for i in range(1, minn + 1):
        if a % i == 0 and b % i == 0:
            ebob = minn
        else:
            ebob -= 1
    return ebob
x = map(int, input('Siyahini daxil edin: ').split())
listt = []
for i in x:
    listt += [i]
mutleq = maxi(listt)
vitse = second_maxi(listt)
ebob = ebob_tap(mutleq, vitse)
print(f'Mutleq Lider: {mutleq}')
print(f'Vitse-Lider: {vitse}')
print(f'Analiz: {mutleq} ve {vitse} ucun ortaq bolenler tapilir...')
print(f'Gizli kod (EBOB): {ebob}')
'''

#Tapsirig 3 Ağıllı Mətn Redaktoru
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
text = input('Metni daxil edin: ') + ' '
yekun = ''
soz = ''
sozler = []
for i in text:
    if i != ' ':
        soz += i
    else:
        if uzun(soz) != 0:
            sozler += [soz]
        soz = ''
for i in sozler:
    if i == 'bad' or i == 'Bad' or i == 'bAd' or i == 'baD' or i == 'BAd' or i == 'BaD' or i == 'bAD' or i == 'BAD':
        yekun += 'good'
    elif '0' <= i <= '9':
        yekun += '*' * int(i)
    else:
        yekun += i
    yekun += ' '
print()
print(f'Netice: {yekun}')
'''

#Tapsirig 4 Maksimum Transformasiya və Rəqəm Balansı
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
def bubble(a):
    n = uzun(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
def reqemayiran(a):
    reqemler = []
    while a:
        reqemler += [a % 10]
        a //= 10
    return reqemler
x = int(input('Bir eded daxil edin: '))
print()
print(f'Ilkin eded: {x}')
yeni = bubble(reqemayiran(x))
max_eded = 0
k = 1
for i in yeni:
    max_eded += i * k
    k *= 10
print(f'Maksimum eded: {max_eded}')
print(f'Ferq: {max_eded - x}')
'''

#Tapsirig 5
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
def reqemsay(a):
    say = 0
    for i in a:
        if '0' <= i <= '9':
            say += 1
    return say
def reqemhasil(a):
    hasil = 1
    if reqemsay(a) == 0:
        return 0
    else:
        for i in a:
            if '0' <= i <= '9':
                hasil *= int(i)
    return hasil
def bubble(a):
    n = uzun(a)
    for i in range(n - 1):
        for j in range(n - 1- i):
            if reqemhasil(a[j]) > reqemhasil(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
            elif reqemhasil(a[j]) == reqemhasil(a[j + 1]):
                if uzun(a[j]) > uzun(a[j + 1]):
                    a[j], a[j + 1] = a[j + 1], a[j]
    return a
cumle = input('Cumleni daxil edin: ') + ' '
yekun = ''
soz = ''
sozler = []
for i in cumle:
    if i != ' ':
        soz += i
    else:
        if uzun(soz) != 0:
            sozler += [soz]
        soz = ''
print(f'Siralanmis netice: ', end = '')
print(*bubble(sozler))
'''
