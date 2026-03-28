#Movzu 2: Sade proqramlar
#Tapsiriq 1 (slide 8)
'''print('Ali')
print('   gezmeye')
print('          gedir')'''

#Tapsiriq 2 (slide 8)
'''print('   J')
print('  JJJ')
print(' JJJJJ')
print('JJJJJJJ')
print(' HH HH')
print(' ZZZZZ')'''

#Tapsiriq (slide 10)
'''a, b = map(int, input('Iki tam eded daxil edin: ').split())
print(f' {a} + {b} = {a + b}')'''

#Movzu 3: Hesablamalar
#Tapsiriq A (slide 39)
'''a, b, c = map(int, input('Uc tam ededi daxil edin: ').split())
print(f' cem --> {a} + {b} + {c} = {a + b + c}')
print(f' hasil --> {a} * {b} * {c} = {a * b * c}')
print(f' ededi orta --> ({a} + {b} + {c}) / 3 = {round((a + b + c) / 3, 3)}')'''

#Tapsiriq B (slide 39)
'''x_a, y_a = map(float, input('A noqtesinin koordinatlarini daxil edin: ').split())
x_b, y_b = map(float, input('B noqtesinin koordinatlarini daxil edin: ').split())
uzunluq = (((x_b - x_a) ** 2) + ((y_b - y_a) ** 2)) ** 0.5
print(f' AB parcasinin uzunlugu = {round(uzunluq, 3)}')'''

#Tapsiriq C (slide 40)
'''from random import randint
a = randint(100,999)
print(f'Tesadufi eded: {a}')
last = a % 10
middle = a // 10 % 10
first = a // 100
print(f' Ededin reqemleri: {first}, {middle}, {last}.')'''

#Movzu 4: Budaqlanma
#Tapsiriq A (slide 49)
'''a, b, c = map(int, input('Uc tam ededi daxil edin: ').split())
if a >= b and a >= c:
    maxx = a
elif a <= b and b >= c:
    maxx = b
elif c >= b and a <= c:
    maxx = c
print(f' En boyuk eded: {maxx}')'''

#Tapsiriq B (slide 49)
'''a, b, c, d, e = map(int, input('Bes tam ededi daxil edin: ').split())
if a >= b and a >= c and a >= d and a >= e:
    maxx = a
elif a <= b and b >= c and b >= d and b >= e:
    maxx = b
elif c >= b and a <= c and c >= d and c >= e:
    maxx = c
elif  d >= a and d >= b and d >= c and d >= e:
    maxx = d
elif  e >= a and e >= b and e >= c and e >= d:
    maxx = e
print(f' En boyuk eded: {maxx}')'''

#Tapsiriq C (slide 50)
'''asif = int(input('Asifin yasini daxil edin: '))
bextiyar = int(input('Bextiyarin yasini daxil edin: '))
vasif = int(input('Vasifin yasini daxil edin: '))
print(f' Asifin yasi: {asif}')
print(f' Bextiyarin yasi: {bextiyar}')
print(f' Vasifin yasi: {vasif}')
if asif > bextiyar and asif > vasif:
    print('Cavab: Asif hamidan yasca boyukdur.')
elif bextiyar > asif and bextiyar > vasif:
    print('Cavab: Bextiyar hamidan yasca boyukdur.')
elif vasif > asif and vasif > bextiyar:
    print('Cavab: Vasif hamidan yasca boyukdur.')
elif bextiyar == asif and bextiyar > vasif:
    print('Cavab: Bextiyar ve Asif Vasifden yasca boyukdurler.')
elif bextiyar == vasif and asif < vasif:
    print('Cavab: Bextiyar ve Vasif Asifden yasca boyukdurler.')
elif asif == vasif and asif > bextiyar:
    print('Cavab: Asif ve Vasif Bextiyardan yasca boyukdurler.')
else:
    print('Cavab: Hamisi eyni yasdadirlar.')'''

#Tapsiriq A (slide 52)
'''a, b, c = map(int, input('Uc ededi daxil edin: ').split())
if a == b and b == c:
    print('Butun ededler eynidir.')
elif (a == b and a != c) or (b == c and c != a) or (a == c and a != b):
    print('Iki eded eynidir.')
else:
    print('Eyni eded yoxdur.')'''

#Tapsiriq B (slide 53)
'''ay = int(input('Ayin nomresini daxil edin: '))
if ay <= 12:
    if ay >= 3 and ay <= 5:
        print(' Yaz.')
    elif ay >= 6 and ay <= 8:
        print(' Yay.')
    elif ay >= 9 and ay <= 11:
        print(' Payiz.')
    else:
        print(' Qis.')
else:
    print(' Ayin nomresi duz deyil.')'''

#Tapsiriq A (slide 54)
'''#a)
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (((x ** 2) + (y ** 2)) >= 4) and y <= x and x <= 2 and y >= 0:
    print(f' ({x},{y}) strixli hisseye DAXILDIR.')
else:
    print(f' ({x},{y}) strixli hisseye daxil DEYILDIR.')
#b)
from math import sin
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (y <= sin(x)) and y >= 0 and y <= 0.5 and x <= 4:
    print(f' ({x},{y}) strixli hisseye DAXILDIR.')
else:
    print(f' ({x},{y}) strixli hisseye daxil DEYILDIR.')'''

#Tapsiriq B (slide 54)
'''#a)
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (((x ** 2) + (y ** 2)) <= 1) and (x <= 0 or y >= x):
    print(f' ({x},{y}) strixli hisseye DAXILDIR.')
else:
    print(f' ({x},{y}) strixli hisseye daxil DEYILDIR.')
#b)
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (y <= (x ** 2)) and ((y >= (2 - x) and (x <= 0)) or (y <= (2 - x) and (x >= 0) and (y >= 0))):
    print(f' ({x},{y}) strixli hisseye DAXILDIR.')
else:
    print(f' ({x},{y}) strixli hisseye daxil DEYILDIR.')
#c)
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (((x ** 2) + (y ** 2) <= 1) and (x >= 0)) or ((x ** 2) + (y ** 2) >= 1) and (y <= 1) and (y >= x - 1) and (x >= 0):
    print(f' ({x},{y}) strixli hisseye DAXILDIR.')
else:
    print(f' ({x},{y}) strixli hisseye daxil DEYILDIR.')'''

#Tapsiriq C (slide 55)
'''#a)
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if ((y >= x ** 2) and (y >= (4 - x ** 2)) and (x >= 0)) or ((y <= x ** 2) and (y >= (2 - x)) and (x <= 0)) or ((y <= (4 - x ** 2)) and (y >= x ** 2) and (y <= (2 - x)) and (x <= 0)) or ((y <= (4 - x ** 2)) and (y <= (2 - x)) and (x >= 0) and (y >= 0) and (y <= x ** 2)):
    print(f' ({x},{y}) strixli hisseye DAXILDIR.')
else:
    print(f' ({x},{y}) strixli hisseye daxil DEYILDIR.')
#b)
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (((x ** 2) + (y ** 2) <= 1) and (y <= 0) and (y >= x)) or ((x ** 2) + (y ** 2) <= 1 and (y <= 0) and (y <= x) and (y >= -x)) or ((x ** 2) + (y ** 2) >= 1 and (y <= 0) and (y <= x) and (y <= -x)) or ((x ** 2) + (y ** 2) <= 1 and (y >= 0) and (y >= x) and (y >= -x)):
    print(f' ({x},{y}) strixli hisseye DAXILDIR.')
else:
    print(f' ({x},{y}) strixli hisseye daxil DEYILDIR.')'''

#Movzu 5: Dovru alqoritmler
#Tapsiriq A (slide 66)
'''a, b = map(int, input('Iki tam ededi daxil edin: ').split())
if a >= 0 and b > a:
    for i in range(a, b + 1):
        print(f' {i}*{i}={i**2}')
else:
    print(' Serte emel edin: (0 < A < B)')'''

#Tapsiriq B (slide 66)
'''a, b = map(int, input('Iki tam ededi daxil edin: ').split())
copy1 = a
copy2 = b
a = abs(a)
b = abs(b)
cavab = 0
for i in range(a):
    cavab += b
if copy1 < 0 and copy2 > 0 or copy1 > 0 and copy2 < 0:
    print(f' {copy1} * {copy2} = {-1 * cavab}')
else:
    print(f' {copy1} * {copy2} = {cavab}')'''

#Tapsiriq C (slide 67)
'''N = int(input('N ededi daxil edin: '))
a = 0
b = 1
c = a + b
cem = 0
for i in range(N):
    while c < N:
        a = b
        b = c
        c = a + b
        cem += b
print(cem)'''

#Tapsiriq A (slide 68)
'''n = int(input('Natural ededi daxil edin: '))
cem = 0
while n > 0:
    digit = n % 10
    n //= 10
    cem += digit
print(f' Reqemlerin cemi {cem}.')'''

#Tapsiriq B (slide 68)
'''n = int(input('Natural ededi daxil edin: '))
while n > 0:
    digit1 = n % 10
    digit2 = n // 10 % 10
    n //= 10
    if digit1 == digit2:
        print(' He.')
        break
else:
    print(' Yox.')'''

#Tapsiriq C (slide 69)
'''n = int(input('Natural ededi daxil edin: '))
copy = n
flag = 0
while copy > 0:
    copy2 = n // 10
    while copy2 > 0:
        digit = n % 10
        if digit == copy2 % 10:
            print('He.')
            flag = 1
            break
        else:
            copy2 //= 10
    copy //= 10
    n //= 10
    if flag == 1:
        break
if flag == 0:
    print('Yox.')'''

#Tapsiriq A (slide 74)
'''print('133-e bolende qaliqda 124, 134-e bolende 111 qalan 5reqemli ededler:', end = ' ')
for i in range(10000,100000):
    if i % 133 == 125 and i % 134 == 111:
        print(i, end = ' ')'''

#Tapsiriq B (slide 74)
'''print('Butun 3reqemli armstronq ededler:', end = ' ')
cem = 0
for i in range(100,1000):
    if (((i % 10) ** 3) + ((i // 10 % 10) ** 3) + ((i // 100)) ** 3) == i:
        print(i, end = ' ')'''

#Tapsiriq C (slide 75)
'''n = int(input('N-i daxil edin: '))
def say(a):
    reqemsay = 0
    while a > 0:
        a //= 10
        reqemsay += 1
    return reqemsay
for i in range(1, n):
    if i == (i ** 2) % (10 ** say(i)):
        print(f' {i} * {i} = {i ** 2}')'''

#Tapsiriq A (slide 81)
'''def sade(a):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        return True
    return False
a, b = map(int, input('Intervalin serhedlerini daxil edin: ').split())
for i in range(a, b + 1):
    if sade(i):
        print(i, end = ' ')'''

#Tapsiriq B (slide 81)
'''print('15, 17 ve 21 kq-liq qutulari acmadan 185 kq unu almagin yollari: ')
usul = 0
for i in range(15):
    for j in range(17):
        for k in range(21):
            if 15 * i + 17 * j + 21 * k == 185:
                usul += 1
                print(f' {usul}. {i} sayda 15 kiloluq, {j} sayda 17 kiloluq ve {k} sayda 21 kiloluq qutular besdir')
print(f' {usul} yol vardir.')'''

#Tapsiriq C (slide 82)
'''n = int(input('N-ni daxil edin: '))
def say(A):
    reqemsay = 0
    while A > 0:
        A //= 10
        reqemsay += 1
    return reqemsay
for i in range(1, n + 1):
    if say(i) == 1:
        if (i % 10 != 0 and i % (i % 10) == 0):
            print(i)
    elif say(i) == 2:
        if (i % 10 != 0 and i // 10 % 10 != 0 and i % (i % 10) == 0) and i % (i // 10 % 10) == 0:
            print(i)
    elif say(i) == 3:
        if (i % 10 != 0 and i // 10 % 10 != 0 and i // 100 % 10 and i % (i % 10) == 0) and i % (i // 10 % 10) == 0 and i % (i // 100 % 10) == 0:
            print(i)
    else:
        break'''

#Movzu 6: Massivler
#Tapsirig A(slide 98)
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0, 100) for i in range(n)]
print('Massiv:')
print(*a)
cem = 0
for j in a:
    cem += j
print(f' Ededi orta: {cem / len(a)}')'''

#Tapsirig B(slide 98)
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0, 100) for i in range(n)]
print('Massiv:')
print(*a)
cem1 = 0
cem2 = 0
say1 = 0
say2 = 0
for j in a:
    if j < 50:
        cem1 += j
        say1 += 1
    else:
        cem2 += j
        say2 += 1
print(f' [0,50) araligindaki element. eded. ort.: {cem1 / say1}')
print(f' [50,100] araligindaki element. eded. ort.: {cem2 / say2}')'''

#Tapsirig C(slide 99)
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = []
while len(a) < n:
    k = randint(1, n)
    if k not in a:
        a += [k]
print('Massiv:')
print(*a)'''

#Movzu 7: Massivlerin emali
#Tapsirig A(slide 104)
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0, 5) for i in range(n)]
print('Massiv:')
print(*a)
x = int(input('Ne axtaririq? '))
for i in range(len(a)):
    if a[i] == x:
        print('Tapildi: ', end = ' ')
        print(f'a[{i}] = {a[i]}')
if n < x:
        print(' Tapilmadi.')'''

#Tapsirig B(slide 105)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,5) for i in range(n)]
print('Massiv:')
print(*a)
flag = 0
for i in range( len(a) - 1):
    if a[i] == a[i+1]:
        flag = 1
        print(f'tapildi {a[i]}')
if flag == 0:
    print('tapilmadi')'''

#Tapsirig C(slide 106)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,5) for i in range(n)]
print('Massiv:')
print(*a)
flag = 0
for i in range(len(a)):
    for k in range(i + 1, len(a)):
        if a[i] == a[k]:
            print('Tapildi:', a[i])
            flag = 1
            break
if flag == 0:
    print('Tapilmadi')'''

#Tapsirig A(slide 110)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,100) for i in range(n)]
print('Massiv:')
print(*a)
def maximum():
    maxx = 0
    for i in range(len(a)):
        if a[i] > maxx:
            maxx = a[i]
            yer = i
    print(f'Maksimal element: a[{yer}]={maxx}')
def minimal():
    minn = a[0]
    for i in range(len(a)):
        if a[i] < minn:
            minn = a[i]
            yer2 = i
    print(f'Minimal element: a[{yer2}]={minn}')
minimal()
maximum()'''

#Tapsirig B(slide 110)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,100) for i in range(n)]
print('Massiv:')
print(*a)
def maximum():
    maxx = 0
    for j in range(2):
        for i in range(len(a)):
            if a[i] > maxx:
                maxx = a[i]
                yer = i
        print(f'Maksimal element: a[{yer}]={maxx}')
        a[yer] = 0
        maxx = 0
maximum()'''

#Tapsirig C(slide 111)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,5) for i in range(n)]
print('Massiv:')
print(*a)
def maximum():
    maxx = 0
    say = 0
    for i in range(len(a)):
        if a[i] > maxx:
            maxx = a[i]
    for i in range(len(a)):
        if a[i] == maxx:
            say += 1
    print(f'Maksimal qiymet {maxx} Element sayi {say}')
maximum()'''

#Tapsirig A(slide 118)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,100) for i in range(n)]
print('Massiv:')
print(*a)
yeni = [a[len(a)-1]] + a[:len(a)-1]
print(*yeni)'''

#Tapsirig B(slide 118)
'''from random import*
n = int(input('Uzunlugu daxil edin:(cut) '))
a = [randint(0,100) for i in range(n)]
print('Massiv:')
print(*a)
if n % 2 == 0:
    ilkyari = n // 2
    for i in range(ilkyari):
        yari = [a[ilkyari-1]] + a[:ilkyari-1]
        ikinciyari = [a[-1]] + a[ilkyari:-1]
    print('Netice: ')
    print(*yari, end=' ')
    print(*ikinciyari)
else:
    print('Say cut olmalidir.')'''

#Tapsirig C(slide 119)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(-100,100) for i in range(n)]
print('Massiv:')
print(*a)
musbeteded = []
menfieded = []
for i in a:
    if i > 0:
        musbeteded += [i]
    else:
        menfieded += [i]
umumi = musbeteded + menfieded
def musbetsay(a):
    say = 0
    for i in a:
        if i > 0:
            say += 1
    return say
print('Netice: ')
print(*umumi)
print(f'Musbet elementlerin sayi: {musbetsay(a)}')'''

#Tapsirig A(slide 122)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(-10,10) for i in range(n)]
b = []
print('A Massivi:')
print(*a)
for i in a:
    if abs(i) % 2 == 0 and i < 0:
        b += [i]
print('B massivi:')
print(*b)'''

#Tapsirig B(slide 122)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,100) for i in range(n)]
b = []
print('A Massivi:')
print(*a)
def sade(a):
    count = 0
    for i in range(2,a):
        if a % i == 0:
            count += 1
    if count == 0:
        return True
    return False
for i in range(len(a)):
    if sade(a[i]):
        b += [a[i]]
print('B massivi:')
print(*b)'''

#Tapsirig C(slide 123)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,100) for i in range(n)]
b = []
print('A Massivi:')
print(*a)
def fibonacci(h):
    bir = 0
    iki = 1
    fibonacciler = [0, 1]
    for i in range(1000):
        uc = bir + iki
        bir = iki
        iki = uc
        fibonacciler += [uc]
    return fibonacciler
for i in a:
    if i in fibonacci(n) and i not in b:
        b += [i]
print('B massivi: ')
print(*b)'''
