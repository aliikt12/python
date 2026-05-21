#Tapsiriq 1
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
def binary(a):
    ikilik = 0
    k = 0
    while a:
        ikilik += (a % 2) * 10 ** k
        k += 1
        a //= 2
    return ikilik
def reqemler(a):
    listt = []
    while a:
        listt += [a % 10]
        a //= 10
    return listt[-1::-1] #[3,4,2,6]
def wavy(a):#3426
    flag = 0
    k = reqemler(a)
    if lenn(k) == 1 or a == 0:
        return False
    for i in range(1, lenn(k) - 1):
        if (k[i - 1] < k[i] and k[i] > k[i + 1]) or (k[i - 1] > k[i] and k[i] < k[i + 1]):
            flag = 1
        else:
            return False
    return True
a = int(input('Start: '))
b = int(input('End: '))
for i in range(a, b + 1):
    if wavy(i) and wavy(binary(i)):
        print(i)
'''

#Tapsiriq 3
'''
def minimum(a):
    minn = float('inf')
    for i in a:
        if i < minn:
            minn = i
    return minn
def maximum(a):
    maxx = float('-inf')
    for i in a:
        if i > maxx:
            maxx = i
    return maxx
from random import randint
n = int(input('Setir: '))
m = int(input('Sutun: '))
a = [[randint(10, 15) for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(f'{a[i][j]:4d}', end = '')
    print()
minler = []
for i in a:
    minler += [minimum(i)]
sutun = []
maxlar = []
for j in range(m):
    for i in range(n):
        sutun += [a[i][j]]
    maxlar += [maximum(sutun)]
flag = 0
for i in maxlar:
    if i in minler:
        print(f'Tapildi: {i}')
        flag = 1
if flag == 0:
    print('Tapilmadi.')
'''

#Tapsiriq 4 abraham->abr brah rah ah ham am
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
def max_uzun(a):
    maxx = float('-inf')
    for i in a:
        if lenn(i) > maxx:
            maxx = lenn(i)
            soz = i
    return soz
text = input('Input: ')
text += text[-1]
i = 0
yeni_kesim = ''
kesimler = []
k = 1
while i < lenn(text):
    if text[i] not in yeni_kesim:
        yeni_kesim += text[i]
        i += 1
    else:
        if yeni_kesim not in kesimler:
            kesimler += [yeni_kesim]
        yeni_kesim = ''
        i = k
        k += 1
print(f'Output: {max_uzun(kesimler)}')   
'''

#Tapsiriq 5
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
def splitt(a):
    a += ' '
    reqem = ''
    reqemler = []
    for i in a:
        if i != ' ':
            reqem += i
        else:
            if lenn(reqem) != 0:
                reqemler += [int(reqem)]
            reqem = ''
    return reqemler
def listcem(a):
    cem = 0
    for i in a:
        cem += i
    return cem
x = input('List 1 elementlerin daxil edin: (bosluqla) ')
y = input('List 2 elementlerin daxil edin: (bosluqla) ')
print('Input:')
list1 = splitt(x)
list2 = splitt(y)
print(f'L1 = {list1}')
print()
print(f'L2 = {list2}')
print()
print('Output:')
k = listcem(list1) % lenn(list2)
list2_yeni = list2[-k::] + list2[:lenn(list2) - k:]
print(f'L2 = {list2_yeni}')
yekun = []
for i in list1:
    if i in list2 and i not in yekun:
        yekun += [i]
print(f'L1 ve L2 arasindaki ortaqlar {yekun}')
'''
