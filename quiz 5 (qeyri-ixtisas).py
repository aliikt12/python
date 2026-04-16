#Tapsiriq 1 Müəyyən olunmuş oblastın tapılması 
'''x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if (y >= (x // 2) ** 2 and y <= 2) or (y - 4) ** 2 + (x + 2) ** 2 <= 0.5 or (y - 4) ** 2 + (x - 2) ** 2 <= 0.5:
    print(f'Daxil edilmis ({x},{y}) koordinati rengli oblasta daxildir.')
else:
    print(f'Daxil edilmis ({x},{y}) koordinati rengli oblasta daxil DEYIL.')'''

#Tapsiriq 2 "Neon" Ədədlərin Filtrasiyası
'''def neon(a):
    cem = 0
    eded = a ** 2
    while eded:
        digit = eded % 10
        cem += digit
        eded //= 10
    return cem
print('Giris:')
print('Eded daxil edin (Dayandirmaq ucun 0 ve ya menfi eded yazin):')
ededler = []
while True:
    a = int(input())
    if a <= 0:
        break
    ededler += [a]
print()
print('Cixis (Output):')
print(f'Daxil edilmis butun ededler: {ededler}')
yekun = []
for i in ededler:
    if neon(i) == i:
        yekun += [i]
print(f'Neon ededlerin siyahisi: {yekun}')'''

#Tapsiriq 3 Şifrələnmiş Siyahının Bərpası
'''def minn(a):
    mini = float('inf')
    for i in range(len(a)):
        if a[i] < mini:
            mini = a[i]
    return mini
print('Giris: ')
say = int(input('Siyahinin uzunlugunu daxil edin: '))
print('Sifrelenmis elementleri daxil edin:')
listt = []
for i in range(say):
    a = int(input())
    listt += [a]
yeni = []
for j in listt:
    yeni += [j - (minn(listt) // 2)]
print()
print('Cixis (Output):')
print('Berpa olunmus siyahi: ', end = '')
print(*yeni)'''

#Tapsiriq 4 "Bol (Abundant)" Ədədlərin Təyini
'''def bolenlercem(a):
    cem = 0
    for i in range(1, a):
        if a % i == 0:
            cem += i
    return cem
bollar = []
nonbollar = []
print('Giris: ')
say = int(input('Siyahinin uzunlugunu daxil edin: '))
print('Ededleri daxil edin:')
listt = []
for i in range(say):
    a = int(input())
    listt += [a]
for i in listt:
    if bolenlercem(i) > i:
        bollar += [i]
    else:
        nonbollar += [i]
print()
print('Cixis (Output):')
print(f'Bol ededler: {bollar}')
print(f'Bol olmayanlar: {nonbollar}')'''

#Tapsiriq 5 "Pilləli" (Stepping) Ədədlərin Axtarışı
'''print('Giris (Input):')
a = int(input('Intervalin baslangici (a): '))
b = int(input('Intervalin sonu (b): '))
pilleliler = []
def pilleli(a):
    flag = 0
    while a:
        digit1 = a % 10
        digit2 = a // 10 % 10
        if abs(digit1 - digit2) == 1:
            a //= 10
            flag = 1
        else:
            a //= 10
            return False
    if flag == 1:
        return True
for i in range(a, b + 1):
    if pilleli(i) and i >= 10:
        pilleliler += [i]
print()
print('Cixis (Output):')
print(f'[{a},{b}] intervalindaki Pilleli ededler: {pilleliler}')'''
