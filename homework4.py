#Homework 4
#Movzu: prosedur, funksiya
#Task 1 Collatz ardicilligi
'''def max_collatz(a):
    print(a, end = ' ')
    maxx = a
    while a != 1:
        if a % 2 == 0:
            a //= 2
            print(a, end = ' ')
            if maxx < a:
                maxx = a
        else:
            a = a * 3 + 1
            print(a, end = ' ')
            if maxx < a:
                maxx = a
    print()
    print(f'Max number: {maxx}')
N = int(input('Enter a number (N>0): '))
max_collatz(N)'''

#Task 2 Çox bölünən ədədlər
'''def length_num(a):
    c = 0
    while a:
        c += 1
        a //= 10
    return c
def is_polydivisible(n, a):
    k = 1
    birsay = 0
    for i in range(1, a + 1):
        reqem = n // (10 ** (a - i))
        print(f'{reqem} % {k} = {reqem % k}')
        if reqem % k != 0:
            birsay += 1
        k += 1
    if birsay != 0:
        print(False)
    else:
        print(True)
n = int(input('Enter a number (N>0): '))
is_polydivisible(n, length_num(n))'''

#Task 3 Bax və nömrələri söylə
'''def length_num(a):
    c = 0
    while a:
        c += 1
        a //= 10
    return c
def look_and_say(a):
    if length_num(a) % 2 == 0:
        num = str(a)
        yekun = ''
        ikiliqruplar = []
        for i in range(0, len(num) - 1, 2):
            ikiliqruplar += [num[i] + num[i + 1]]
        for j in range(len(ikiliqruplar)):
            tekrarlanan = ikiliqruplar[j][1]
            tekrarsay = ikiliqruplar[j][0]
            yekun += tekrarlanan * int(tekrarsay)
        print(yekun)
    else:
        print('invalid')
n = int(input('Enter a number (N>0): '))
look_and_say(n)'''

#Task 4 Onluq və ikilik palindrom
'''def is_Palindrome(a):
    copy1 = a
    copy2 = a
    yeni = 0
    c = 0
    while a:
        c += 1
        a //= 10
    while copy1:
        digit = copy1 % 10
        copy1 //= 10
        yeni += digit * (10 ** c)
        c -= 1
    yeni //= 10
    if yeni == copy2:
        return True
    else:
        return False
def to_Binary(a):
    ikilik = 0
    i = 0
    while a:
        eded = a % 2
        a //= 2
        ikilik += eded * (10 ** i)
        i += 1
    return str(ikilik)
def Palindrome_type(a):
    if is_Palindrome(a) == True and is_Palindrome(int(to_Binary(a))) == False:
        print('Palindrome type is only Decimal.')
    elif is_Palindrome(a) == False and is_Palindrome(int(to_Binary(a))) == False:
        print('Palindrome type is neither Decimal nor Binary.')
    elif is_Palindrome(a) == True and is_Palindrome(int(to_Binary(a))) == True:
        print('Palindrome type is Decimal and Binary.')
    else:
        print('Palindrome type is only Binary.')
n = int(input('Enter a number (N>0): '))
print(f'Decimal: {n}')
print(f'Binary: {to_Binary(n)}')
Palindrome_type(n)'''

#Task 5 n – tam ədədini və p-natural ədədini qəbul edib k ədədini çap edən funksiya
'''def length_num(a):
    c = 0
    while a:
        c += 1
        a //= 10
    return c
def np_to_k(n, p):
    copy = n
    cavab = 0
    reqem = str(n)
    reqem = reqem[-1::-1]
    reqem = int(reqem)
    i = 0
    while reqem:
        digit = reqem % 10
        reqem //= 10
        cavab += digit ** (p + i)
        i += 1
    yekun = cavab // copy
    if yekun == 0:
        print('None')
    else:
        print(f'K: {yekun}')
n = int(input('Enter N: '))
m = int(input('Enter M: '))
np_to_k(n, m)'''
