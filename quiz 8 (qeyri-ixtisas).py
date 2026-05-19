#Tapsirig 1 "Morze-Binary" Kodlaşdırması
'''
def binary(a):
    ikilik = 0
    k = 0
    while a:
        ikilik += (a % 2) * 10 ** k
        k += 1
        a //= 2
    return ikilik
def morse(a):
    morze = ''
    tire = 0
    while a:
        if (a % 10) == 0:
            morze += '.'
        else:
            tire += 1
            morze += '-'
        a //= 10
    return morze, tire
def polindrom(a):
    yeni = ''
    for i in a:
        yeni = i + yeni
    if yeni == a:
        return True
    return False
x = int(input('Onluq eded daxil edin: '))
print()
print('Tehlil:')
print(f'1. Ikilik qarsiligi: {binary(x)}')
print(f'2. Morze kodu: {morse(binary(x))[0]}')
print(f'3. Tirelerin (-) sayi: {morse(binary(x))[1]}')
print()
print('Netice')
if polindrom(morse(binary(x))[0]):
    print('Bu bir "Simmetrik Siqnal"dir! (Polindrom)')
else:
    print('Bu bir "Qeyri-Simmetrik Siqnal"dir!')
'''

#Tapsirig 2 "Cüt Rəqəm Süzgəci" və Siyahı Sıralaması
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
def suzme(a):
    yeni = 0
    k = 0
    while a:
        if (a % 10) % 2 == 0:
            yeni += (a % 10) * 10 ** k
            k += 1
        a //= 10
    return yeni
def bubble(a):
    n = uzun(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if suzme(a[j]) > suzme(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
x = map(int, input('Ededleri daxil edin: ').split())
print()
listt = []
for i in x:
    listt += [i]
print('Tehlil:')
for i in listt:
    print(f'- {i} -> Suzulmus: {suzme(i)}')
print()
print('Siralama Prosesi (Suzulmus deyere gore):')
k = 1
for i in range(uzun(bubble(listt))):
    print(f'{k}. {listt[i]} \t(Suzulmus: {suzme(listt[i])})')
    k += 1
print()
print('Netice:', end = ' ')
print(*bubble(listt))
'''

#Tapsirig 3 "Siyahı Statistikası" (Moda və Median)
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
def max_tekrar(a):
    maxx = float('-inf')
    for i in a:
        say = 0
        for k in a:
            if i == k:
                say += 1
        if maxx < say:
            maxx = say
    return say
def sayan(a, k):
    say = 0
    for i in a:
        if i == k:
            say += 1
    return say
def moda(a):
    modalar = []
    for i in a:
        if sayan(a, i) == max_tekrar(a) and i not in modalar:
            modalar += [i]
    return modalar
def bubble(a):
    n = uzun(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
x = map(int, input('Siyahi elementlerini daxil edin (bosluqla): ').split())
listt = []
for i in x:
    listt += [i]
print()
print(f'Daxil edilmis siyahi: {listt}')
print()
print('Tehlil:')
print(f'1. Siyahinin uzunlugu: {uzun(listt)}')
print(f'2. En yuksek tekrar sayi: {max_tekrar(listt)}')
print(f'3. Tapilan Modalar: {moda(listt)}')
k = moda(listt)
print(f'4. Siralanmis siyahi: {bubble(listt)}')
if uzun(listt) % 2 == 0:
    number1 = listt[(uzun(listt) // 2) - 1]
    number2 = listt[uzun(listt) // 2]
    median = (number1 + number2) // 2
    print(f'5. Median hesabi: ({number1} + {number2}) // 2: {(number1 + number2) // 2}')
else:
    median = listt[(uzun(listt) // 2)]
    print(f'5. Median hesabi: {listt[(uzun(listt) // 2)]}')
print()
print('Neticeler:')
print(f'Modalar: {k}')
print(f'Median: {median}')
'''

#Tapsirig 4 "Rəqəmsal Transformasiya" və Bubble Sort
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c
def kodlasdirma(a):
    numbers = '1234567890'
    kod = ''
    for i in range(uzun(a)):
        if a[i] not in numbers:
            kod += str(i)
        else:
            kod += a[i]
    return kod
def reqemcem(a):
    a = int(a)
    cem = 0
    while a:
        cem += a % 10
        a //= 10
    return cem
def bubble(a):
    n = uzun(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if reqemcem(a[j]) > reqemcem(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
cumle = input('Cumleni daxil edin: ') + ' '
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
print('Tehlil:')
k = 1
kodlari = []
for i in sozler:
    print(f'{k}. "{i}" -> "{kodlasdirma(i)}", Ceki: {reqemcem(kodlasdirma(i))}')
    kodlari += [kodlasdirma(i)]
    k += 1
print()
print('Siralama (Cekiye gore artan):')
for i in bubble(kodlari):
    print(f'{i} (Ceki: {reqemcem(i)})')
print()
print('Netice:')
for i in kodlari:
    print(i, end = ' ')
'''

#Tapsirig 5 Matrisin "Riyazi Simmetriyası"
'''
def sade(a):
    if a < 2:
        return False
    else:
        c = 0
        for i in range(2, a):
            if a % i == 0:
                c += 1
        if c == 0:
            return True
        return False
def polindrom(a):
    copy = a
    yeni = 0
    while a:
        yeni = (yeni * 10) + a % 10
        a //= 10
    if yeni == copy:
        return True
    return False
from random import randint
n = int(input('N-i daxil edin: '))
a = [[randint(10,15) for i in range(n)] for i in range(n)]
print('Yaradilmis random matris:')
for i in a:
    print(i)
print()
print('Tehlil:')
cem = 0
for i in range(n):
    if sade(a[i][i]):
        cem += a[i][i]
print(f'1. Esas diaqonaldaki sade ededlerin cemi: {cem}')
saypolindrom = 0
for i in range(n):
    if polindrom(a[i][n - 1 - i]):
        saypolindrom += 1
print(f'2. Komekci diaqonaldaki polindromlarin sayi: {saypolindrom}')
murekkeb = 0
for j in range(n):
    if j % 2 == 0:
        for i in range(n):
            if not sade(a[i][j]):
                murekkeb += 1
print(f'3. Cut sutunlardaki murekkeb ededlerin sayi: {murekkeb}')
print()
print('Neticeler:')
print(f'Sade Cem: {cem}')
print(f'Polindrom Sayi: {saypolindrom}')
print(f'Murekkeb Sayi: {murekkeb}')
'''
