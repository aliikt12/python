#3rd week exercise
#1
'''
from random import randint
for i in range(5):
    for j in range(10):
        print(f'{randint(1,50):4d}', end = ' ')
    print()
'''

#2
'''
def maxi(a):
    maxx = float('-inf')
    for i in a:
        if i > maxx:
            maxx = i
    return maxx
def mini(a):
    minn = float('inf')
    for i in a:
        if i < minn:
            minn = i
    return minn
from random import randint
a = [[randint(1, 100) for i in range(10)] for i in range(5)]
for i in range(5):
    for j in range(10):
        print(f'{a[i][j]:4d}', end = ' ')
    print(f'Maximumu: {maxi(a[i])}, minimumu: {mini(a[i])}')
'''

#3
'''
def cemi(a):
    cem = 0
    for i in a:
        cem += i
    return cem
from random import randint
a = [[randint(1, 100) for i in range(10)] for i in range(5)]
for i in range(5):
    for j in range(10):
        print(f'{a[i][j]:4d}', end = ' ')
    print(f'Setrin cemi: {cemi(a[i])}')
'''

#4
'''
def cemi(a):
    cem = 0
    for i in a:
        cem += i
    return cem
from random import randint
a = [[randint(1, 100) for i in range(10)] for i in range(5)]
for i in range(5):
    for j in range(10):
        print(f'{a[i][j]:4d}', end = ' ')
    print(f'Setrin cemi: {cemi(a[i]) / 10}')
'''

#5
'''
usul = 0
for i in range(21):
    for j in range(21):
        if 5 * i + 7 * j == 100:
            usul += 1
            print(f'{usul}. {i} dene 5 kq-liq, {j} dene 7 kq-liq.')
'''

#6
'''
usul = 0
for i in range(70):
    for j in range(40):
        for k in range(20):
            for h in range(10):
                if 8 * i + 16 * j + 32 * k + 64 * h == 512:
                    usul += 1
print(f'{usul} sayda muxtelif usul vardir.')       
'''

#7
'''
def maxi(a):
    maxx = float('-inf')
    for i in a:
        if i > maxx:
            maxx = i
    return maxx
def mini(a):
    minn = float('inf')
    for i in a:
        if minn > i:
            minn = i
    return minn
a = []
while True:
    x = input("Enter a number ('Exit' to quit): ")
    if x == 'Exit':
        break
    else:
        a += [int(x)]
print(f'Ededlerin en boyuyu: {maxi(a)}, en kiciyi: {mini(a)}')
'''

#8
'''
def uzun(a):
    c = 0
    for i in a:
        c += 1
    return c  
def reqemler(a):
    listt = []
    while a:
        listt += [a % 10]
        a //= 10
    return listt
for eded in range(1000, 1501):
    cemcut = 0
    cemtek = 0
    x = reqemler(eded)
    for i in range(uzun(x)):
        if i % 2 == 0:
            cemcut += x[i]
        else:
            cemtek += x[i]
    if cemcut == cemtek:
        print(eded)
'''

#9
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()
'''

#10
'''
for i in range(1, 6):
    for j in range(6 - i, 0, -1):
        print(i, end = ' ')
    print()
'''

#11
'''
for i in range(1, 6):
    for j in range(6 - i, 0, -1):
        print(5, end = ' ')
    print()
'''

#12
'''
k = 0
for i in range(1, 10, 2):
    k += 1
    for j in range(1, k + 1):
        print(i, end = ' ')
    print()
'''

#13
'''
k = 10
for i in range(1, 6):
    print(' ' * k, end = '')
    for j in range(1, i + 1):
        print(j, end = ' ')
    k -= 2
    print()
'''

#14
'''
k = 9
for i in range(1, 6):
    print(' ' * k, end = '')
    for j in range(1, i + 1):
        print('*', end = ' ')
    print()
    k -= 2
'''

#15
'''
k = 6
for i in range(1, 7):
    print(' ' * k, end = '')
    for j in range(7 - i, 0, -1):
        print('*', end = ' ')
    k += 1
    print()
'''

#16
'''
for i in range(1, 7):
    for j in range(1, i + 1):
        print('*', end = ' ')
    print()
print()
for i in range(1, 7):
    for j in range(7 - i, 0, -1):
        print('*', end = ' ')
    print()
'''

#17
'''
k = 8
for i in range(1, 6):
    print(' ' * k, end = '')
    for j in range(1, i + 1):
        print('*', end = ' ')
    k -= 2
    print()
k = 2
for i in range(1, 5):
    print(' ' * k, end = '')
    for j in range(5 - i, 0, -1):
        print('*', end = ' ')
    print()
    k += 2
'''
