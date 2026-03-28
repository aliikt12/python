#1 5-10 araliginda 7 ve 9 dan basga ededleri cap eden proqram
'''print('[5-10] araligindaki 7 ve 9-dan basga olan ededler:')
i = 5
while i <= 10:
    if i == 7 or i == 9:
        i += 1
        continue
    print(i, end = ' ')
    i += 1'''

#2 0 daxil edilene qeder daxil edilen ededlerin cemini cap eden proqram
'''cem = 0
while True:
    a = int(input('Enter a number: '))
    if a == 0:
        break
    cem += a
print(f' Daxil edilen ededlerin cemi = {cem}')'''

#3 -1 yazilanadek daxil edilen ededlerin ededi ortasini cap eden proqram
'''cem = 0
say = 0
while True:
    a = int(input('Enter a number: '))
    if a == -1:
        break
    cem += a
    say += 1
print(f' Daxil edilen ededlerin ededi ortasi = {cem/say}')'''
    
#4 Daxil edilen natural ededin reqemleri cemini capa veren proqram
'''a = int(input('Natural ededi daxil edin: '))
cem = 0
while a > 0:
    digit = a % 10
    cem += digit
    a //= 10
print(f' Reqemlerin cemi {cem}.')'''

#5 Polindrom ededi yoxlayan proqram
'''a = int(input('Ededi daxil edin: '))
copy = a
yeni = 0
say = 0
while a > 0:
    digit = a % 10
    a //= 10
    say += 1
i = 10 ** say
a = copy
while a > 0:
    digit = a % 10
    a //= 10
    yeni += digit * i
    i //= 10
if (yeni // 10) == copy:
    print(f' {copy} --> {yeni // 10} polindrom ededdir.')
else:
    print(f' {copy} --> {yeni // 10} polindrom eded DEYIL.')'''

#6 iki qonsu reqemi olan ededi yoxlayan proqram
'''a = int(input('Natural ededi daxil edin:'))
while a > 0:
    digit1 = a % 10
    digit2 = a // 10 % 10
    a //= 10
    if digit1 == digit2:
        print('- He.')
        break
else:
    print('- Yox.')'''

#7 Bütün üç rəqəmli Armstronq ədədlərini tapan proqram
'''i = 100
print('Ucreqemli Armstronq ededler:', end = ' ')
while i < 1000:
    digit1 = i % 10
    digit2 = i // 10 % 10
    digit3 = i // 100
    if (digit1 ** 3 + digit2 ** 3 + digit3 ** 3) == i:
        print(i, end = ' ')
        i += 1
    else:
        i += 1'''

#8 ededi sade vuruqlarina ayiran proqram
'''a = int(input('Ededi daxil edin: '))
print('Ededin sade vuruqlari: ', end = '')
def sade(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count == 0 and n != 1:
        return True
    return False
i = 2
while a >= i:
    if a % i == 0 and sade(i):
        print(i, end = ' ')
        a = a // i
        i = 2
    else:
        i += 1'''

#9 2likden 10luga ceviren proqram
'''ikilik = int(input('Ededi ikilik say sisteminde daxil edin: '))
copy = ikilik
onluq = 0
i = 0
while ikilik > 0:
    digit = ikilik % 10
    onluq += digit * (2 ** i)
    i += 1
    ikilik //= 10
print(f' Daxil edilen ikilik eded ({copy}) onluq kodu = {onluq}')'''

#10 10luqdan 2liye ceviren proqram
'''onluq = int(input('Ededi onluq say sisteminde daxil edin: '))
copy = onluq
ikilik = 0
quvvet = 1
while onluq > 0:
    digit = onluq % 2
    onluq //= 2
    ikilik += digit * quvvet
    quvvet *= 10
print(f' Daxil edilen onluq eded ({copy}) ikilik kodu = {ikilik}')'''

#11 [0, 50] aralığında Fibonaççi ardıcıllığını ekrana çıxaran proqram
'''print('[0-50] araligindaki Fibonacci ardicilligi: ', end = '')
n = 0
a = 0
b = 1
c = a + b
print(b, end = ' ')
while c < 50:
    print(c, end = ' ')
    a = b
    b = c
    c = a + b'''

#12 N ədədi istifadəçi tərəfindən daxil edilərək, aşağıdakı cəmi hesablayan və nəticəni ekrana çıxaran proqram 
'''N = int(input('N ededini daxil edin: '))
#a bendi
cavab = 0
n = 0
while n <= N:
    cavab += (n) / ((1 + (n ** 3)) ** 0.5)
    n += 1
print(f' a) bendinde ifadenin cavabi N-in {N} qiymetinde {cavab}-dir.')
#b bendi
cavab = 0
quvvet = 1
while quvvet <= N:
    cavab += (quvvet ** quvvet) / (quvvet)
    quvvet += 1
print(f' b) bendinde ifadenin cavabi N-in {N} qiymetinde {cavab}-dir.')
#c bendi
cavab = 0
n = 1
while n <= N:
    cavab += ((1.1 ** n) + (n ** 2)) / (5 * n)
    n += 1
print(f' c) bendinde ifadenin cavabi N-in {N} qiymetinde {cavab}-dir.')'''

#13 Daxil edilmiş ədədin üzərində onun rəqəmlərini toplamaq, rəqəmlərini vurmaq və yaxud əməliyyatı ləğv etmək üçün seçim istəyən bir proqram 
'''print('1.) Reqemleri topla')
print('2.) Reqemleri vur')
print('3.) Cixmaq ucun hansisa duymeye bas')
print()
eded = int(input('2 reqemli eded daxil edin: '))
secim = int(input('Bir secim edin: '))
if secim == 1:
    cem = 0
    while eded > 0:
        digit = eded % 10
        cem += digit
        eded //= 10
    print(cem)
elif secim == 2:
    hasil = 1
    while eded > 0:
        digit = eded % 10
        hasil *= digit
        eded //= 10
    print(hasil)
else:
    exit()'''

#14 Natural N ədədi daxil edən və N-dən böyük olmayan bütün avtomorf ədədləri ekrana çıxardan proqram
'''n = int(input('N-i daxil edin:'))
i = 1
def say(a):
    reqemsay = 0
    while a > 0:
        reqemsay += 1
        a //= 10
    return reqemsay
while i <= n:
    for j in range(10):
        if i == ((i ** 2) % 10 ** say(i)):
            print(f' {i} * {i} = {i ** 2}')
            i += 1
        else:
            i += 1'''

#15 N natural ədədi daxil edin. N-dən böyük olmayan və öz rəqəmlərinin hər birinə bölünən proqram
'''n = int(input('N-ni daxil edin: '))
i = 1
def say(a):
    reqemsay = 0
    while a > 0:
        reqemsay += 1
        a //= 10
    return reqemsay
while i <= n:
    if say(i) == 1:
        if i % 10 != 0 and i % (i % 10) == 0:
            print(i)
            i += 1
        else:
            i += 1
    elif say(i) == 2:
        if i % 10 != 0 and i % (i % 10) == 0 and i % (i // 10 % 10) == 0:
            print(i)
            i += 1
        else:
            i += 1
    elif say(i) == 3:
        if i % 10 != 0 and i // 10 % 10 != 0 and i % (i % 10) == 0 and i % (i // 10 % 10) == 0 and i % (i // 100 % 10) == 0:
            print(i)
            i += 1
        else:
            i += 1
    else:
        break'''
