#Task 1 “Mükəmməl ədədlər”
'''
def bolenler(a):
    bolen = []
    for i in range(1, a):
        if a % i == 0:
            bolen += [i]
    return bolen
def listcem(a):
    cem = 0
    for i in a:
        cem += i
    return cem
def mukemmel(a):
    if listcem(bolenler(a)) == a:
        return True
    return False
a = int(input('Enter start: '))
b = int(input('Enter end: '))
total = 0
for i in range(a, b + 1):
    if mukemmel(i):
        total += 1
        print(f'Perfect number found: {i}')
        print('Divisors: ', end = '')
        print(*bolenler(i))
print(f'Total found: {total}')
'''

#Task 2 "Zəncirvari Harshad" ədədləri
'''
def sum_digits(a):
    cem = 0
    while a:
        cem += a % 10
        a //= 10
    return cem
def harshad_chain(a):
    while a / sum_digits(a) != 1:
        if a % sum_digits(a) == 0:
            a = sum_digits(a)
        else:
            return False
    return True
x = int(input('Enter a number (N>0): '))
if harshad_chain(x):
    i = 1
    while True:
        if x / sum_digits(x) == 1:
            print(f'Step {i} : {x} / {sum_digits(x)} = {x / sum_digits(x)}')
            break
        print(f'Step {i} : {x} / {sum_digits(x)} = {x / sum_digits(x)}')
        i += 1
        x = x // sum_digits(x)
    print(f'Total chain length: {i}')
else:
    print('Not in harshad chain')
'''

#Task 3 "İkili-Onluq Dominantlığı"
'''
def max_digit(a):
    maxx = float('-inf')
    while a:
        if a % 10 > maxx:
            maxx = a % 10
        a //= 10
    return maxx
def count_binary_ones(a):
    ikilik = 0
    k = 0
    while a:
        ikilik += (a % 2) * 10 ** k
        k += 1
        a //= 2
    birsay = 0
    while ikilik:
        if ikilik % 10 == 1:
            birsay += 1
        ikilik //= 10
    return birsay
def is_dominant_trip(a):
    if max_digit(a) == count_binary_ones(a):
        return True
    return False
x = int(input('Enter a number (N>0): '))
print(f'Max digit: {max_digit(x)}')
print(f'Binary ones count: {count_binary_ones(x)}')
if is_dominant_trip(x):
    print('Result: True. It is a Dominant Trip number.')
else:
    print('Result: False. It is not a Dominant Trip number.')
'''

#Task 4 "Sirkulyar-İkilik Analizator"
'''
def len_number(a):
    c = 0
    while a:
        c += 1
        a //= 10
    return c
def rotate_number(a):
    first = a // 10 ** (len_number(a) - 1)
    yeni = first
    k = 1
    while a > 9:
        yeni += (a % 10) * 10 ** k
        k += 1
        a //= 10
    return yeni
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
def binary_weight_type(a):
    ikilik = 0
    birsay = 0
    k = 0
    while a:
        ikilik += (a % 2) * 10 ** k
        k += 1
        a //= 2
    while ikilik:
        if ikilik % 10 == 1:
            birsay += 1
        ikilik //= 10
    if birsay % 2 == 0:
        return 2
    elif birsay % 2 == 1:
        return 1
    else:
        return 0
def bolencem(a):
    cem = 0
    for i in range(1, a):
        if a % i == 0:
            cem += i
    return cem
def perfect(a):
    if a % bolencem(a) == 0:
        return True
    return False
def analyze_complex_number(a):
    if sade(a) and sade(rotate_number(a)):
        return 'Result: Category A'
    elif not(sade(a)) and binary_weight_type(a) == 2:
        return 'Result: Category B (Composite with Even Binary Weight)'
    elif perfect(a):
        return 'Result: Category C'
    else:
        return 'Result: Category D'
x = int(input('Enter a number (N>0): '))
print(f'Original: {x}')
print(f'Rotated: {rotate_number(x)}')
print(f'Binary Weight Type: {binary_weight_type(x)}')
print(analyze_complex_number(x))
'''

#Task 5 Faktorial Cəmi və Xoşbəxtlik Analizi
'''
def fakt(a):
    hasil = 1
    for i in range(1, a + 1):
        hasil *= i
    return hasil
def get_factorial_sum(a):
    cem = 0
    while a:
        cem += fakt(a % 10)
        a //= 10
    return cem
def is_happy(a):
    cem = 0
    while True:
        if cem == 4:
            return False
        else:
            while a:
                cem += (a % 10) ** 2
                a //= 10
            a = cem
            cem = 0
        if a == 1:
            return True
n = int(input('N natural ededini daxil: '))
print('------------------------------')
print(f'Faktorial Cemi (int): {get_factorial_sum(n)}')
print(f'Xosbextdirmi? (bool): {is_happy(n)}')
'''
