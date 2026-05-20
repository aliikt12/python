#Mock 2
#1
'''
from math import sin
x = float(input('Enter x: '))
y = float(input('Enter y: '))
if ((x ** 2) + (y ** 2)) <= 30 and (y >= -3 and y <= sin(x) and x >= -5 and y >= 2 * x - 3) or (y >= sin(x) and y <= 2 * x - 3):
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
cumle = input('Write a sentence: ') + ' '
soz = ''
sozler = []
for i in cumle:
    if i != ' ':
        soz += i
    else:
        if lenn(soz) != 0:
            sozler += [soz]
        soz = ''
print(f'Number of words: {lenn(sozler)}')
'''

#3
'''
def sade(a):
    if a < 2:
        return False
    else:
        c = 0
        for i in range(2, a):
            if a % i == 0:
                c += 1
        if c == 0:
            return True
        return False
def my_function(my_list):
    new_list = []
    count = 0
    for i in my_list:
        if sade(i):
            new_list += [i]
        else:
            count += 1
    return new_list, count
from random import randint
a = [randint(10, 99) for i in range(20)]
print(f'List: {a}')
print(f'Prime number list: {my_function(a)[0]}')
print(f'Number of non-prime numbers: {my_function(a)[1]}')
'''
