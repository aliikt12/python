#Tapsiriq 1 Müəyyən olunmuş oblastın tapılması
'''print('Giris:')
x = float(input('x koordinatini daxil edin: '))
y = float(input('y koordinatini daxil edin: '))
print()
print('Cixis (Output):')
if (y >= x and y <= 4 and x >= 0 and y >= 1 / x) or (y <= x and y >= -4 and x <= 0 and y <= 1 / x):
    print('Oblasta daxildir')
else:
    print('Oblasta daxil deyil')'''

#2 Ən Böyük 3 Rəqəmli Ədəd
'''def maxx(a):
    maxx = 0
    while a:
        digit = a % 10
        if maxx < digit:
            maxx = digit
        a //= 10
    return maxx
def minn(a):
    minn = 9
    while a:
        digit = a % 10
        if minn > digit:
            minn = digit
        a //= 10
    return minn
def yenieded(i):
    return 900 + maxx(i) * 10 + minn(i)
print('Giris:')
a = int(input('Bir eded daxil edin: '))
print()
print('Cixis (Output):')
print(f'En boyuk reqem: {maxx(a)}')
print(f'En kicik reqem: {minn(a)}')
print(f'Yaradilan 3 reqemli eded: {yenieded(a)}')'''

#Tapsiriq 3 Poli-Kvadrat Ədədlərin Tapılması
'''def tersine_cevir(n):
    return int(str(n)[-1::-1])
def is_palindrome(n):
    if tersine_cevir(n) == n:
        return True
    return False
a = int(input('Start daxil edin: '))
b = int(input('End daxil edin: '))
print('Giris')
print(f'Araliq: {a} - {b}')
print()
print('Cixis (Output):')
for i in range(a, b + 1):
    if is_palindrome(i) == True and is_palindrome(i ** 2) == True:
        print(f'{i} (kvadrati: {i ** 2})')'''

#Tapsiriq 4 İkilik Ədədin Analizi və Sadəlik Yoxlanışı
'''def is_prime(a):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        return True
    return False
def to_decimal(a):
    onluq = 0
    i = 0
    while a:
        digit = a % 10
        onluq += digit * (2 ** i)
        i += 1
        a //= 10
    return onluq
def is_binary(a):
    while a:
        digit = a % 10
        if digit > 1:
            return False
        a //= 10
    return True
print('Giris:')
ikilik = int(input('Ikilik eded daxil edin: '))
print()
print('Cixis:')
if is_binary(ikilik):
    print(f'1. Onluq qarsiligi: {to_decimal(ikilik)}')
    if is_prime(to_decimal(ikilik)):
        print(f'2. Analiz neticesi: {to_decimal(ikilik)} sade ededdir.')
    else:
        print(f'2. Analiz neticesi: {to_decimal(ikilik)} sade eded deyildir.')
else:
    print('Eded ikilik say sisteminde deyildir.')'''

#Tapsiriq 5 Super-Harshad Ədədlərin tapılması
'''def reqem_cemi(n):
    cem = 0
    while n:
        digit = n % 10
        cem += digit
        n //= 10
    return cem
def is_perfect_square(n):
    if (n ** 0.5) % 1 == 0:
        return True
    return False
def is_super_harshad(a):
    qismet = a / reqem_cemi(a)
    if is_perfect_square(qismet):
        return True
a = int(input('Start daxil edin: '))
b = int(input('End daxil edin: '))
print('Giris')
print(f'Araliq: {a} - {b}')
print()
print('Cixis (Output):')
for i in range(a, b + 1):
    if is_super_harshad(i):
        print(f'Eded: {i}', end = '   ')
        print(f'| Sert: {i} / {reqem_cemi(i)} = {i // reqem_cemi(i)}')'''
