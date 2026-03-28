#1 a^x ifadesini hesablayan proqram(** olmaz)
'''a = int(input('Ededi daxil edin: '))
x = int(input('Quvveti daxil edin: '))
cavab = 1
for i in range(1, x + 1):
    cavab *= a
print(f' {a}^{x} = {cavab}')'''

#2 a! hesablayan proqram
'''a = int(input('Ededi daxil edin: '))
hasil = 1
for i in range(1, a+1):
    hasil *= i
print(f' {a}! = {hasil}')'''

#3 [1,50] intervalindaki cut ededleri cap eden proqram
'''print('[1-50] intervalindaki cut ededler:')
for i in range(1, 51):
    if i % 2 == 0:
        print(i)'''

#4 1-N araligindaki ededleri cemleyen proqram
'''N = int(input('N-i daxil edin: '))
cem = 0
for i in range(1, N + 1):
    cem += i
print(f' 1-N araligindaki ededlerin cemi = {cem}')'''

#5 1 – X + X^2 – X^3 …. X^N sırasının cəmini hesablayan proqram
'''X = int(input('X-i daxil edin: '))
N = int(input('N-i daxil edin: '))
cavab = 0
for i in range(N + 1):
    cavab += ((-1) ** i) * (X ** i)
print(cavab)'''

#6 1-100 araligindaki ededleri azalan sirada cap eden proqram
'''print('[1-100] araligindaki ededlerin azalma sirasi: ')
for i in range(100, 0, -1):
    print(i)'''

#7 0-10 araligindaki ededleri ve kvadratlarini cap eden proqram
'''print('[0-10] araligindaki ededler ve onlarin kvadratlari:')
for i in range(0, 11):
    print(f' {i}-->{i**2}')'''

#8 0-10 aralığında olan cüt ədədlərin cəmini tapın, tək ədədlərin isə hasilini tapan proqram
'''print('[0-10] araligindaki cut ededlerin cemi ve tek ededlerin hasili:')
cem = 0
hasil = 1
for i in range(0, 11):
    if i % 2 == 0:
        cem += i
    else:
        hasil *= i
print(f' cut ededlerin cemi = {cem} ve tek ededlerin hasili = {hasil}')'''

#9 A-B aralığında C-yə bölünən ədədləri ekrana çıxaran proqram
'''a = int(input('A-ni daxil edin: '))
b = int(input('B-ni daxil edin: '))
c = int(input('Boleni daxil edin: '))
if a > b:
    print(f' [{b},{a}] araliginda {c}-e bolunen ededler: ') 
    for i in range(b, a + 1):
        if i % c == 0:
            print(f' {i}')
else:
    if a < b:
        print(f' [{a},{b}] araliginda {c}-e bolunen ededler: ')
        for i in range(a, b + 1):
            if i % c == 0:
                print(f' {i}')
    else:
        print(' Verilen araliq dogru deyil')'''

#10 A-B aralığında olan cüt və tək ədədlərin sayını tapan proqram
'''a = int(input('A-ni daxil edin: '))
b = int(input('B-ni daxil edin: '))
cut = 0
tek = 0
if a < b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            cut += 1
        else:
            tek += 1
    print(f' [{a},{b}] araligindaki cut eded sayi = {cut}, tek eded sayi = {tek}-dir')
else:
    if a > b:
        for i in range(b, a + 1):
            if i % 2 == 0:
                cut += 1
            else:
                tek += 1
        print(f' [{b},{a}] araligindaki cut eded sayi = {cut}, tek eded sayi = {tek}-dir')
    else:
        print(' Verilen araliq dogru deyil')'''

#11 1-100 aralığında təsadüfi götürülən 10 ədədin cüt və ya tək olduğunu gösteren proqram
'''from random import randint
print('[1,100] araligindaki tesadufi 10 ededin tekliyi ve cutluyu:')
for i in range(10):
    x = randint(1, 100)
    if x % 2 == 0:
        print(f' {x}-->cut')
    else:
        print(f' {x}-->tek')'''

#12 İki tam A və B ədədi (0 < A < B) qəbul edən və [A, B] intervalında bütün natural ədədlərin kvadratını hesablayan proqram 
'''a = int(input('A-ni daxil edin: '))
b = int(input('B-ni daxil edin: '))
if a > 0 and b > a:
    for i in range(a, b + 1):
        print(f' {i} * {i} = {i ** 2}')
else:
    print(' Serte emel edin(0<A<B)')'''

#13 İki tam ədədi qəbul edən və vurma əməliyyatdan istifadə etmədən ədədlərin hasilini xaric edən proqram (menfi daxil)
'''a = int(input('Birinci ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
hasil = 0
if a > 0 and b > 0:
    for i in range(a):
        hasil += b
elif (a > 0 and b < 0) or (a < 0 and b > 0):
    for i in range(abs(a)):
        hasil += abs(b)
    hasil *= -1
elif a < 0 and b < 0:
    for i in range(abs(a)):
        hasil += abs(b)
print(f' {a} * {b} = {hasil}')'''

#14 pi ededini ilk 15 addimda hesablayan proqram
'''print('Pi ededinin teqribi qiymeti: ', end='')
pi = 3
k = 2
for i in range(15):
    pi += ((-1) ** i) * (4 / (k * (k + 1) * (k + 2)))
    k += 2
print(pi)'''

#15 133-ə böləndə qalıqda 125, 134-də böləndə qalıqda 111 alınan bütün beş rəqəmli ədədləri təyin eden proqram
'''print('133-e bolende qaliqda 125, 134-e bolende ise 111 alinan butun 5reqemli ededler: ')
for i in range(10000,100000):
    if i % 133 == 125 and i % 134 == 111:
        print(i)'''

#16 2 ededin EBOBu
'''#1ci versiya
from math import gcd
a = int(input('Birinci ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
print(gcd(a,b))'''

'''#2ci versiya
a = int(input('Birinci ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
if a >= 1 and b >= 1 and a != b:
    if a > b:
        minn = b
        print(f' EBOB({b},{a}) =', end=' ')
    else:
        minn = a
        print(f' EBOB({a},{b}) =', end=' ')
    while True:
        if a % minn == 0 and b % minn == 0:
            print(minn)
            break
        else:
            minn -= 1
else:
    print(' Xeta')'''

#17 A-B intervalindaki sade ededleri cap eden proqram
'''a = int(input('Ilk ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
if a < b and a > 0 and b > 0:
    print(f' Intervalin serhedleri: {a} {b}')
    for i in range(a, b + 1):
        bolen = 0
        for j in range(1, i + 1):
            if i % j == 0:
                bolen += 1
        if bolen == 2:
            print(i, end = ' ')
else:
    print(' Xeta')'''

#18 15,17 ve 21 kgliq qutulari acmadan 185 kg unun nece ferqli usulla alinmasini gosteren proqram
'''print('Magazada 15, 17 ve 21 kq-liq qutularda un satilir. 185 kq unu almagin muxtelif yollari ')
usul = 0
nomre = 1
for i in range(14):
    for j in range(12):
        for k in range(11):
            if 15 * i + 17 * j + 21 * k == 185:
                print(f' {nomre}. {i} dene 15 kiloluq, {j} dene 17 kiloluq, {k} dene 21 kiloluq 185 kiloqram eder.')
                usul += 1
                nomre += 1
print(f'{usul} sayda yolla etmek olar.')'''
