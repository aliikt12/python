#Homework 5
#Movzu: Setirler
#Task 1 Boşluqları silən proqram
'''text = input('Enter a sentence: ') + ' '
yekun = ''
soz = ''
sozler = []
for i in text:
    if i != ' ':
        soz += i
    else:
        if len(soz) != 0:
            sozler += [soz]
        soz = ''
for i in sozler:
    yekun += i + ' '
print('The modified string is:')
print(yekun)'''

#Task 2 Parity bit – Uyğunluq biti
'''def onecounter(a):
    count = 0
    for i in a:
        if i == '1':
            count += 1
    if count % 2 == 0:
        return 'cut'
    else:
        return 'tek'
while True:
    x = input('Enter 8 bits: ')
    if x == 'end':
        break
    elif len(x) != 8:
        print('That was not 8 bits ... Try again')
    else:
        if onecounter(x) == 'cut':
            print('The parity bit should be 0')
        else:
            print('The parity bit should be 1')'''

#Task 3 Pig Latin dili
'''text = input('Enter a line of text: ')
def pig_latin_translation(a):
    consonant = 'qwrtypsdfghjklzxcvbnm'
    vowels = 'aeuio'
    if a[0] in consonant:
        for i in range(len(a)):
            if a[i] in vowels:
                part2 = a[0:i] + 'ay'
                part1 = a[i::]
                break
        pig_latin = part1 + part2
        return pig_latin
    else:
        return a + 'way'
print(f'Translated text: {pig_latin_translation(text)}')'''

#Task 4 Yaşayış binası
'''floor = int(input('Floors (must be at least 2): '))
width = int(input('Width (excluding walls, must be a non-zero even integer): '))
roof = input("Roof type ('flat' or 'pointy'): ")
def draw_roof(a, b):
    yekun = ' '
    k = a
    if b == 'flat':
        for i in range(a):
            yekun += '_'
        print(yekun)
    else:
        for i in range(a // 2):
            print(' ' * (a // 2 - i) + '/' + ' ' * i * 2 + '\\')
draw_roof(width, roof)
def draw_floor(a):
    yekun = ''
    for i in range(floor - 1):
        print('|' + ' '*width + '|')
draw_floor(floor)
def draw_ground_floor(a):
    yekun = '|'
    for i in range(1, a):
        if i == a // 2:
            yekun += '||'
        else:
            yekun += ' '
    yekun += '|'
    return yekun
print(draw_ground_floor(width))
def draw_base(a):
    yekun = ''
    for i in range(a + 2):
        yekun += '='
    return yekun
print(draw_base(width))'''

#Task 5 Reddit Username Check
'''
name = input('Enter a username: ')
def is_neighbour_numbers(a):
    numbers = '0123456789'
    for i in range(len(a) - 1):
        if a[i - 1] in numbers and a[i] in numbers and a[i + 1] in numbers:
            if a[i - 1] == a[i] and a[i] == a[i + 1]:
                return True
    return False
def is_letter_exist(a):
    numbers = '1234567890'
    for i in range(len(a)):
        if ('A' <= a[i] <= 'Z' or 'a' <= a[i] <= 'z') and a[i] not in numbers:
            return True
    return False
def is_number_exist(a):
    for i in range(len(a)):
        if '0' <= a[i] <= '9':
            return True
    return False
def is_neighbour_letters(a):
    for i in range(1, len(a) - 1):
        if is_letter_exist(a[i - 1]) and is_letter_exist(a[i]) and is_letter_exist(a[i + 1]):
            return True
    return False
def is_space_exist(a):
    for i in range(len(a)):
        if a[i] <= ' ':
            return True
    return False
def is_beginning_digit(a):
    numbers = '0123456789'
    if a[0] in numbers:
        return True
    return False
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
    print('Wrong! Name cannot start with digit!')
if flag == 0:
    print('Correct username!')
'''
