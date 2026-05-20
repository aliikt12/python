#Task 1 Ədədin rəqəmləri, rəqəmləri cəmi və hasili
'''
def reqemler(a):
    if a < 0:
        a = -a
    listt = []
    while a:
        listt += [a % 10]
        a //= 10
    return listt[::-1]
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
x = int(input('Enter 4 digit number: '))
print('Digits:', end = ' ')
k = reqemler(x)
print(*k)
print('Sum of digits: ', end = '')
cem = 0
for i in range(lenn(k)):
    cem += k[i]
    if i != lenn(k) - 1:
        print(f'{k[i]} +', end = ' ')
    else:
        print(f'{k[i]} = {cem}')
print('Product of digits: ', end = '')
hasil = 1
for i in range(lenn(k)):
    hasil *= k[i]
    if i != lenn(k) - 1:
        print(f'{k[i]} *', end = ' ')
    else:
        print(f'{k[i]} = {hasil}')
'''

#Task 2
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
def polindrom(a):
    r = ''
    for i in a:
        r = i + r
    if a == r:
        return True
    return False
text = input('Polindrom_kombinasiya: ') + ' '
soz = ''
sozler = []
for i in text:
    if i != ' ':
        soz += i
    else:
        if lenn(soz) != 0:
            sozler += [soz]
        soz = ''
poliler = []
for i in range(lenn(sozler)):
    for j in range(lenn(sozler)):
        yoxla = sozler[i] + sozler[j]
        if polindrom(yoxla) and yoxla not in poliler:
            poliler += [yoxla]
print(f'Cixis: {poliler}')
'''

#Task 3 Zooparka giriş qiyməti
'''
total = 0
while True:
    x = input("Enter the age of guest ('end' to quit): ")
    if x == 'end':
        break
    else:
        if int(x) <= 2:
            total += 0
        elif 3 <= int(x) <= 12:
            total += 14
        elif int(x) >= 65:
            total += 18
        else:
            total += 23
print(f'The total for that group is ${total}')
'''

#Task 4 Çox bölünən ədədlər
'''
def length_num(a):
    c = 0
    while a:
        c += 1
        a //= 10
    return c
def is_polydivisible(a):
    b = length_num(a)
    k = 1
    for i in range(b):
        if (a // (10 ** (length_num(a) - k))) % k == 0:
            k += 1
        else:
            return False
    return True
x = int(input('Enter a number (N>0): '))
k = 1
for i in range(length_num(x)):
    print(f'{x // (10 ** (length_num(x) - k))} % {k} = {(x // (10 ** (length_num(x) - k))) % k}')
    k += 1
print(is_polydivisible(x))
'''

#Task 5 Reddit Username Check
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
def is_neighbour_numbers(a):
    numbers = '0123456789'
    for i in range(lenn(a) - 2):
        if a[i] in numbers and a[i + 1] in numbers and a[i + 2] in numbers:
            return True
    return False
def is_letter_exist(a):
    for i in a:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            return True
    return False
def is_number_exist(a):
    for i in a:
        if '0' <= i <= '9':
            return True
    return False
def is_neighbour_letters(a):
    for i in range(lenn(a) - 2):
        if is_letter_exist(a[i]) and is_letter_exist(a[i + 1]) and is_letter_exist(a[i + 2]):
            return True
    return False
def is_space_exist(a):
    for i in a:
        if i == ' ':
            return True
    return False
def is_beginning_digit(a):
    if '0' <= a[0] <= '9':
        return True
    return False
name = input('Enter a username: ')
flag = 0
if is_neighbour_numbers(name):
    print('Wrong! There cannot be 3 sequential numbers!')
    flag = 1
if not(is_letter_exist(name)):
    print('Wrong! There should be at least one letter!')
    flag = 1
if not(is_number_exist(name)):
    print('Wrong! There should be at least one digit!')
    flag = 1
if is_neighbour_letters(name):
    print('Wrong! There cannot be 3 sequential letters!')
    flag = 1
if is_space_exist(name):
    print('Wrong! There cannot be an empty space!')
    flag = 1
if is_beginning_digit(name):
    print('Wrong! Name cannot start with digit')
    flag = 1
if flag == 0:
    print('Correct username!')
'''

#Task 6
'''
def lenn(a):
    c = 0
    for i in a:
        c += 1
    return c
def bubble(a):
    n = lenn(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lenn(a[j]) > lenn(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    return a[-1]
def en_uzun_altsetir(a):
    a += a[-1]
    yekun = ''
    yekunlar = []
    i = 0
    k = 1
    while i < lenn(a):
        if a[i] not in yekun:
            yekun += a[i]
            i += 1
        else:
            yekunlar += [yekun]
            yekun = ''
            i = k
            k += 1
    return bubble(yekunlar)
x = input('Giris: ')
print(f'Cixis: {en_uzun_altsetir(x)}')
'''
