#1 Oblast
'''
from math import sin
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (((x ** 2) + (y ** 2)) <= 30) and ((y <= sin(x) and y >= -3 and x >= -5 and y >= 2 * x - 3) or (y >= sin(x) and y <= 2 * x - 3)):
    print(f'({x},{y}) noqtesi renglenmis hisseye DAXILDIR!')
else:
    print(f'({x},{y}) noqtesi renglenmis hisseye DAXIL DEYIL!')
'''

#2 Silsilə Sadə Ədədlər
'''
def sade(a):
    c = 0
    for i in range(2, a):
        if a % i == 0:
            c += 1
    if c == 0 and a != 1:
        return True
    return False
cem = 0
n = int(input('Nece eded daxil edeceksiniz? '))
for i in range(1, n + 1):
    x = int(input(f'{i}-ci ededi daxil edin: '))
    if sade(x):
        print(f'({x} sadedir, ceme elave olundu)')
        cem += x
    else:
        print(f'({x} sade deyil! Proses dayandirilir.)')
        break
    if i == n:
        print('Proses dayandirilir ...')
print()
print('-------------------------')
print(f'Yekun cem: {cem}')
'''

#3 Rəqəm Köklərinin Tapılması
'''
def reqemcem(a):
    cem = 0
    while a:
        cem += a % 10
        a //= 10
    return cem
x = int(input('Analiz ucun eded daxil edin: '))
print()
i = 1
while True:
    print(f'Addim {i}: {x} reqemleri cemi = {reqemcem(x)}')
    if reqemcem(x) >= 10:
        x = reqemcem(x)
        i += 1
    else:
        break
print('--------------------------')
print(f'Yekun Reqem Koku: {reqemcem(x)}')
print(f'Cemi Addim Sayi: {i}')
'''

#4 "Dinamik Armstrong Aralığı"
'''
def uzun(a):
    say = 0
    while a:
        say += 1
        a //= 10
    return say
def armstrong(a):
    copy = a
    cem = 0
    while a:
        cem += (a % 10) ** uzun(copy)
        a //= 10
    if cem == copy:
        return True
    return False
start = int(input('Starti daxil edin: '))
end = int(input('Endi daxil edin: '))
print(f'{start} ve {end} araligindaki Armstrong ededleri:')
say = 0
for i in range(start, end + 1):
    if armstrong(i):
        print(f'Tapildi: {i} (Reqem sayisi: {uzun(i)}')
        say += 1
print()
print(f'Cemi {say} Armstrong ededi tapildi.')
'''

#5 "Səkkizlik-İkilik Balans Analizatoru"
'''
def octalcem(a):
    sekkizlik = 0
    i = 0
    while a:
        sekkizlik += a % 8 * 10 ** i
        a //= 8
        i += 1
    cem = 0
    while sekkizlik:
        cem += sekkizlik % 10
        sekkizlik //= 10
    return cem
def ikilikbir(a):
    ikilik = 0
    i = 0
    while a:
        ikilik += a % 2 * 10 ** i
        a //= 2
        i += 1
    say = 0
    while ikilik:
        if ikilik % 10 == 1:
            say += 1
        ikilik //= 10
    return say
x = int(input('Analiz ucun eded daxil edin: '))
print()
print('------------------------------')
print(f'Daxil edilen eded (Onluq): {x}')
print(f'Sekkizlik reqemlerinin cemi: {octalcem(x)}')
print(f"Ikilik '1'-lerin sayi: {ikilikbir(x)}")
if octalcem(x) == ikilikbir(x):
    print('Netice: True (Eded BALANSLIDIR)')
else:
    print('Netice: False (Eded Balansli DEYIL)')
'''
