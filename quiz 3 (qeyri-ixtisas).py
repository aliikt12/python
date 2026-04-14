#Tapsiriq 1 Daxil edilən nöqtələrin verilən oblasta aid olub olmamasını yoxlayan proqram
'''x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (((x ** 2) + (y ** 2)) <= 20) and ((x >= 0 and y <= 0) or (x >= 0 and y >= 0 and y <= x + 1)):
    print(f'({x},{y}) koordinati verilen oblasta DAXILDIR.')
else:
    print(f'({x},{y}) koordinati verilen oblasta DAXIL DEYILDIR.')'''

#Tapsiriq 2 Silsile cut bolenlerin cemi
'''ededsay = int(input('Nece eded daxil edeceksiniz? '))
print()
for i in range(1, ededsay + 1):
    cem = 0
    cutbolenler = []
    eded = int(input(f'{i}. ededi daxil edin: '))
    if eded > 0:
        for j in range(1, eded + 1):
            if eded % j == 0 and j % 2 == 0:
                cutbolenler += [j]
        if len(cutbolenler) == 0:
            print(f'(Cut bolen yoxdur, ', end = '')
        for k in range(len(cutbolenler)):
            cem += cutbolenler[k]
            if cutbolenler[k] == cutbolenler[-1]:
                print(f'{cutbolenler[k]} =', end = ' ')
            elif cutbolenler[k] == cutbolenler[0]:
                print(f'({cutbolenler[k]}+', end = '')
            else:
                print(f'{cutbolenler[k]}+', end = '')

        print(f'{cem})')
        print()
    else:
        print('(Eded uygun deyil! Proses dayandirilir.)')'''

#Tapsiriq 3 Reqemlerin hasili prosesi
'''n = int(input('Analiz ucun eded daxil edin: '))
print()
i = 1
while True:
    reqem = str(n)
    copy = n
    reqem = reqem[-1::-1]
    n = int(reqem)
    sonreqem = reqem[0]
    hasil = 1
    k = 0
    if n > 0:
        print(f'Addim {i}: ', end = '')
        while k < len(str(copy)):
            digit = n % 10
            n //= 10
            hasil *= digit
            if digit == int(sonreqem):
                print(f'{digit} = {hasil}')
            else:
                print(f'{digit} *', end = ' ')
            k += 1
        i += 1
        yekun_hasil = hasil
        if hasil >= 10:
            n = hasil
        else:
            break
print()
print('-------------------------')
print(f'Yekun netice: {yekun_hasil}')
print(f'Cemi addim sayi: {i - 1}')'''

#4 Dinamik Güclü Ədədlər Aralığı
'''def fakt(a):
    hasil = 1
    for i in range(1, a + 1):
        hasil *= i
    return hasil
def reqemfakthasil(a):
    cavab = 0
    while a:
        digit = a % 10
        a //= 10
        cavab += fakt(digit)
    return cavab
a = int(input('Start daxil edin: '))
b = int(input('End daxil edin: '))
print()
print('Guclu ededler')
for i in range(a, b + 1):
    if reqemfakthasil(i) == i:
        print(i)'''

#5 Onluq-İkilik Paritet Aralığı(Sert ve output uygun deyil)
'''def reqemcem(a):
    cem = 0
    while a:
        digit = a % 10
        cem += digit
        a //= 10
    return cem
def ikilik(a):
    ikilik = 0
    count = 0
    i = 0
    while a:
        r = a % 2
        ikilik += r * 10 ** i
        i += 1
        a //= 2
    while ikilik:
        if ikilik % 10 == 1:
            count += 1
        ikilik //= 10
    return count
a = int(input('Start daxil edin: '))
b = int(input('End daxil edin: '))
print()
print('Uygun ededler')
for i in range(a, b + 1):
    if reqemcem(i) % 2 == 0 and ikilik(i) % 2 == 0:
        print(i)'''
