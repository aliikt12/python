#1 Noqtenin koordinat analizi
'''x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
print(f' Noqte: ({x},{y})')
if (x ** 2 + y ** 2) <= 1 and (y >= (6 * (x ** 2))) and (y >= abs(2 * x)) and (y >= 0.5):
    print(' Netice: Noqte qirmizi rengli oblasta DAXILDIR.')
else:
    print(' Netice: Noqte qirmizi rengli oblasta DAXIL DEYILDIR.')'''

#2 Silsile sade ededler
'''cem = 0
bolen = 0
while True:
    a = int(input('Enter a number: '))
    for i in range(2, a):
        if a % i == 0:
            bolen += 1
    if bolen == 0 and a != 1:
        cem += a
        print(f' {a} sadedir, davam edirik...')
    else:
        print(f' {a} sade deyil, proqram dayanir!')
        print(f'Total sum of prime numbers: {cem}')
        break'''

#3 Reqem koklerinin tapilmasi
'''step = 1
def cem(a):
    summ = 0
    while a > 0:
        digit = a % 10
        summ += digit
        a //= 10
    return summ
a = int(input('Enter a number: '))
while cem(a) > 10:
    print(f' Step {step}: {cem(a)}')
    a = cem(a)
    step += 1
print(f'Step {step}: {cem(a)}')
print(f'Digital root: {cem(a)}')
print(f'Total steps: {step}')''' 

#4 Binary Mirror
'''a = int(input('Enter a number: '))
lastdigit = a % 10
print(f'Last digit: {lastdigit}')
def ikilik(a):
    ikilik = 0
    quvvet = 1
    while a > 0:
        qaliq = a % 2
        ikilik += qaliq * quvvet
        quvvet *= 10
        a //= 2
    return ikilik
birsayi = 0
b = ikilik(a)
while b > 0:
    digit = b % 10
    b //= 10
    if digit == 1:
        birsayi += 1
print(f'Binary ones count: {birsayi}')
if birsayi == lastdigit:
    print('Result: True. It is a Mirror number.')
else:
    print('Result: False. It is not a Mirror number.')'''

#5 Ucqat Suzgecli Binary Analizator
'''n = int(input('Enter a number (N): '))
copy = n
print()
print('--- ANALIZ PROSESI ---')
def sade(a):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        return True
    return False
def ikilik(a):
    ikilik = 0
    quvvet = 1
    birsayi = 0
    while a > 0:
        qaliq = a % 2
        ikilik += qaliq * quvvet
        quvvet *= 10
        a //= 2
    while ikilik > 0:
        digit = ikilik % 10
        ikilik //= 10
        if digit == 1:
            birsayi += 1
    if birsayi % 2 == 1:
        return birsayi
    else:
        return birsayi
def ikilik2(a):
    ikilik = 0
    quvvet = 1
    while a > 0:
        qaliq = a % 2
        ikilik += qaliq * quvvet
        quvvet *= 10
        a //= 2
    return ikilik
ind = ikilik(n)
if sade(n) == True and ind > 3:
    print(f'1. Orijinal eded ({n}) sadedir? BELI.')
    print(f'2. {n}-in binary formasi ({ikilik2(n)}) nece dene "1" saxlayir? {ikilik(n)} (3-den boyukdur).')
    print('Seviyye 3')
elif sade(n) == True and ind % 2 == 1:
    print(f'1. Orijinal eded ({n}) sadedir? BELI.')
    print(f'2. {n}-in binary formasi ({ikilik2(n)}) nece dene "1" saxlayir? {ikilik(n)} (Tekdir).')
    print('Seviyye 1')
elif sade(n) == False:
    cem = 0
    while n > 0:
        reqem = n % 10
        cem += reqem
        n //= 10
    if cem % 5 == 0:
        print(f'1. Orijinal eded ({copy}) sadedir? XEYR.')
        print(f'2. {copy}-in reqemleri cemi ({cem}) 5-e tam bolunur? BELI!')
        print('Seviyye 2')
    elif ind > 3:
        print(f'1. Orijinal eded ({copy}) sadedir? XEYR.')
        print(f'2. {copy}-in binary formasi ({ikilik2(copy)}) nece dene "1" saxlayir? {ikilik(copy)} (3-den boyukdur).')
        print('Seviyye 3')'''
