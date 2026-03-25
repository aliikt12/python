#1 (-1) daxil edilənədək əldə olunan natural ədədlərin cəminin cüt və ya tək olduğunu göstərən funksiya
'''def function():
    cem = 0
    while True:
        a = int(input('Enter a number: '))
        if a == -1:
            break
        cem += a
    if cem % 2 == 0:
        print(f' Netice: {cem}-cutdur.')
    else:
        print(f' Netice: {cem}-tekdir.')
function()'''

#2 (a, b) ədədləri daxil edilir. a ədədini b ədədinə böldükdə alınan qismət cüt olarsa, True, əks halda False cavabını qaytaran funksiya 
'''def function(a, b):
    r = a // b
    if r % 2 == 0:
        print(True)
    else:
        print(False)
a = int(input('a-ni daxil edin: '))
b = int(input('b-ni daxil edin: '))
function(a, b)'''

#3 Giriş olaraq (n, k) ədədləri daxil edilir. əgər k^k=n şərti doğru olarsa, True, əks halda False cavabını qaytaran funksiya 
'''def function(n, k):
    if k ** k == n:
        print(True)
    else:
        print(False)
n = int(input('n ededini daxil edin: '))
k = int(input('k ededini daxil edin: '))
function(n, k)'''

#4 Ədədin pronic və ya heteromecic olmasını müəyyənləşdirən funksiya 
'''def pronic(a):
    eded = 0
    for n in range(1, a + 1):
        if n * (n + 1) == a:
            eded = True
    if eded == True:
        print(f' {a} pronic ededdir.')
    else:
        print(f' {a} heteromecic ededdir.')
n=int(input('Enter a number: '))
pronic(n)'''

#5 Tam ədədin uzunluğunu – rəqəmlərinin sayını təyin edən funksiya 
'''def count(a):
    say = 0
    a = abs(a)
    if a == 0:
        say = 1
    while a > 0:
        say += 1
        a //= 10
    return say
a = int(input('Enter a number: '))
print(count(a))'''

#6 N ədədinin Disarium ədəd olub-olmadığını təyin edən funksiya 
'''def say(a):
    count = 0
    while a > 0:
        count += 1
        a //= 10
    return count
def disarium(a):
    cem = 0
    quvvet = say(a)
    copy = a
    while a > 0:
        cem += (a % 10) ** quvvet
        quvvet -= 1
        a //= 10
    if cem == copy:
        print(f' Daxil edilen {copy} ededi disarium ededdir.')
    else:
        print(f' Daxil edilen {copy} ededi disarium eded DEYIL.')
a = int(input('Enter a number: '))
disarium(a)'''
        
#7 Curzon ədədi teyin eden funksiya 
'''def curzon(a):
    if ((2 ** a) + 1) % (2 * a + 1) == 0:
        print(f' Daxil edilen {a} ededi curzon ededdir.')
    else:
        print(f' Daxil edilen {a} ededi curzon eded DEYIL.')
a = int(input('Enter a number: '))
curzon(a)'''

#8 Kempner ededleri teyin eden funksiya
'''def fakt(a):
    hasil = 1
    for i in range(2, a + 1):
        hasil *= i
    return hasil
n = int(input('Enter a number: '))
for j in range(1, n + 1):
    if fakt(j) % n == 0:
        print(f' {n}-->{j}!')
        break'''
    
#9 Moran ədədini təyin edən funksiya 
'''def cem(a):
    summ = 0
    while a > 0:
        summ += a % 10
        a //= 10
    return summ
def sade(a):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        return True
    return False
a = int(input('Enter a number: '))
copy = a
qismet = copy // cem(a)
if copy % cem(a) == 0 and sade(qismet) == True:
    print(f' {copy} --> Moran')
else:
    print(f' {copy} --> Non-Moran')'''

#10 İstənilən daxil edilmiş ədədin birinci və sonuncu rəqəmlərinin cəminin kvadrat kökünün 3-dən böyük olanlarını yoxlayan məntiqi funksiya 
'''a = int(input('Enter a number: '))
def funksiya(a):
    lastdigit = a % 10
    a //= 10
    while a > 0:
        digit = a % 10
        a //= 10
    firstdigit = digit
    kvkok = (lastdigit + firstdigit) ** (1/2)
    if kvkok > 3:
        print(True)
    else:
        print(False)
funksiya(a)'''

#11 Daxil edilmiş ədədlərin qarşılıqlı sadə ədədlər olub-olmadığını müəyyən edən məntiqi funksiya
'''def qarsiliqlisade(a, b):
    if a >= 1 and b >= 1:
        if a > b:
            minn = b
        else:
            minn = a
        while True:
            if a % minn == 0 and b % minn == 0:
                ebob = minn
                break
            else:
                minn += -1
        if ebob == 1:
            print(f' True! {a} ve {b} qarsiliqli sade ededlerdir.')
        else:
            print(f' False! {a} ve {b} qarsiliqli sade ededler DEYIL.')
a, b = map(int, input('iki natural eded daxil edin: ').split())
qarsiliqlisade(a, b)'''

#12 Daxil edilmiş ədədin hiper-sadə ədəd olub olmadığını müəyyən edən məntiqi funksiya 
'''def sade(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count == 0 and n != 1:
        return True
    return False
def hipersade(a):
    copy = a
    while a > 0:
        if sade(a):
            a //= 10
        else:
            print(f' {copy} ededi hiper-sade deyil.')
            break
    if a < 10 and sade(a):
        print(f' {copy} ededi hiper-sadedir.')
p = int(input('Natural ededi daxil edin: '))
hipersade(p)'''

#13 İki natural ədədin ƏBOB və ƏKOB-nu hesablayan funksiya
'''a, b = map(int, input('Iki natural eded daxil edin: ').split())
def ebob(x, y):
    if x > y:
        minn = y
    else:
        if x < y:
            minn = x
        else:
            print(' Xeta')
    while True:
        if x % minn == 0 and y % minn == 0:
            ebob = minn
            break
        else:
            minn -= 1
    return ebob
def ekob(x, y):
    ekob = (x * y) // ebob(x, y)
    return ekob
print(f' Daxil edilen {a} ve {b} ededleri ucun EBOB({a},{b}) = {ebob(a, b)} ve EKOB({a},{b}) = {ekob(a, b)}')'''

#14 Daxil edilmiş üç ədədi artan sıra ilə düzən funksiya
'''a, b, c = map(int, input('Uc natural eded daxil edin: ').split())
def muqayise(a, b, c):
    if a >= b and a >= c:
        maxx = a
    elif a <= b and b >= c:
        maxx = b
    elif c >= b and a <= c:
        maxx = c
    if a <= b and a <= c:
        minn = a
    elif a >= b and b <= c:
        minn = b
    elif c <= b and a >= c:
        minn = c
    qalan = a + b + c - maxx - minn
    print(minn, qalan, maxx)
muqayise(a, b, c)'''

#15 M/N kəsrini sadələşdirən funksiya
'''M, N = map(int, input('Kesrin suret ve mexrecini daxil edin: ').split())
def sadelesdirme(a, b):
    if a > b:
        minn = b
    else:
        if b > a:
            minn = a
        else:
            print(' Xeta')
    while True:
        if a % minn == 0 and b % minn == 0:
            ebob = minn
            break
        else:
            minn -= 1
    print(f'{a // minn}/{b // minn}')
sadelesdirme(M, N)'''

#16 Ədədi tərsinə yazan funksiya
'''n = int(input('Natural ededi daxil edin: '))
def say(q):
    reqemsay = 0
    while q > 0:
        reqemsay += 1
        q //= 10
    return reqemsay
def tersine(a):
    yeni = 0
    quvvet = 10 ** say(a)
    while a > 0:
        digit = a % 10
        a //= 10
        yeni += digit * quvvet
        quvvet //= 10
    return yeni // 10
print(tersine(n))'''
    

    
