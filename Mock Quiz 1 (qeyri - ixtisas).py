#Mock 1
#1
'''
def modul(A):
    if A < 0:
        return -A
    return A
x = float(input('Enter x: '))
y = float(input('Enter y: '))
if ((x ** 2) + (y ** 2)) <= 1 and y >= 0.5 and y >= (6 * x ** 2) and y >= modul(2 * x):
    print('Daxildir!')
else:
    print('Daxil DEYIL!')
'''

#2
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
text = input('Text: ')
ne = input('What to change: ')
neile = input('To what to change: ')
yekun = ''
i = 0
while i < lenn(text):
    if text[i:i + lenn(ne)] == ne:
        yekun += neile
        i += lenn(ne)
    else:
        yekun += text[i]
        i += 1
print(yekun)
'''

#3
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
def ilk_cut(a):
    cem = 0
    for i in range(lenn(a)):
        if a[i] % 2 == 1:
            cem += a[i]
        elif a[i] % 2 == 0:
            return a[i], i, cem
from random import randint
n = int(input('How many elements: '))
if n % 3 != 0:
    print('Error')
else:
    a = [randint(10, 99) for i in range(n)]
    print(f'List = {a}')
    print(f'Listin ilk cut elementi: A[{ilk_cut(a)[1]}] = {ilk_cut(a)[0]}')
    print(f'Cem: {ilk_cut(a)[2]}')
    yekun = []
    i = 0
    while i < lenn(a):
        tupp = a[i:i + 3]
        yekun += [tuple(tupp)]
        i += 3
    print(f'B: {yekun}')
'''
