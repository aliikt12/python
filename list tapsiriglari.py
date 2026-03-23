#Tapsirig A(slide 98)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,100) for i in range(n)]
print('Massiv:')
print(*a)
cem = 0
for c in a:
    cem += c
print(f'Ədədi orta: {cem/len(a)}')'''

#Tapsirig B(slide 98)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,100) for i in range(n)]
print('Massiv:')
print(*a)
s1=0
c1=0
s2=0
c2=0
for j in a:
    if j < 50:
        s1 += 1
        c1 += j
    else:
        s2 += 1
        c2 += j
print(f'[0,50) araligi ucun={c1/s1}')
print(f'[50,100] araligi ucun={c2/s2}')'''

#Tapsirig C(slide 99)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = []
while len(a) < n:
    k = randint(1,n)
    if k not in a:
        a += [k]
print('Massiv: ')
print(*a)'''

#Tapsirig A(slide 104)
'''from random import*
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0,5) for i in range(n)]
print('Massiv:')
print(*a)
x = int(input('Ne axtaririq: '))
for i in range( len(a) ):
    if a[i] == x:
        print('Tapildi: ', end=' ')
        print(f'a[{i}]-->{a[i]}')
if n < x:
    print('tapilmadi.')'''

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

    












