#Homework 1
#Movzu: Sade proqramlar, hesablamalar
#Task 1 Qiymetin hesablanmasi
'''a = int(input('Notebook: '))
a1 = float(input('Notebook price (azn): '))
b = int(input('Pencil: '))
b1 = float(input('Pencil price (azn): '))
print(f' {a} notebooks and {b} pencils total price: {a * a1 + b * b1} azn')'''

#Task 2 Zaman
'''m = int(input('Minute: '))
h = m // 60
m1 = m - (h * 60)
print(f' {m} minutes = {h} hours {m1} minutes')'''

#Task 3 Ededin reqemleri cemi ve hasili
'''a = int(input('Enter 4 digit number: '))
print(f' Digits: {a // 1000} {a // 100 % 10} {a // 10 % 10} {a % 10}')
print(f' Sum of digits: {a // 1000} + {a // 100 % 10} + {a // 10 % 10} + {a % 10} = {a // 1000 + a // 100 % 10 + a // 10 % 10 + a % 10}')
print(f' Product of digits: {a // 1000} * {a // 100 % 10} * {a // 10 % 10} * {a % 10} = {(a // 1000) * (a // 100 % 10) * (a // 10 % 10) * (a % 10)}')'''    

#Task 4 Ucbucagin sahesi
'''s1 = float(input('Side 1: '))
s2 = float(input('Side 2: '))
s3 = float(input('Side 3: '))
if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print('Bele ucbucaq yoxdur.')
else:
    if (s1 < s2 + s3 and s1 > abs(s2 - s3)) and (s2 < s1 + s3 and s2 > abs(s1 - s3)) and (s3 < s2 + s1 and s3 > abs(s2 - s1)):
        s = (s1 + s2 + s3) / 2
        area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
        print(f' Area of triangle: {round(area, 2)}')
    else:
        print('Bele ucbucaq yoxdur.')'''

#Task 5 Emeliyyatlar
'''from math import log10
a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(f' {a} + {b} = {a + b}')
print(f' {a} - {b} = {a - b}')
print(f' {a} * {b} = {a * b}')
print(f' {a} % {b} = {a % b}')
print(f' {a} // {b} = {a // b}')
print(f' {a} ** {b} = {a ** b}')
print(f' log10( {a} ) = {round(log10(a), 2)}')'''

#Task 6 Cem ucun dustur
'''a = int(input('Enter a number: '))
result = (a * (a + 1)) / 2
print(f' Result: {result}')'''

#Task 7 Coxbucaqlinin sahesi
'''from math import tan, pi
length = int(input('Length: '))
side = int(input('Number of sides: '))
area = (side * (length ** 2)) / (4 * tan(pi / side))
print(f' Area: {round(area, 5)}')'''

#Task 8 Selsi -> Farenheyt
'''c = int(input('Temperature (C): '))
f = (c * 1.8) + 32
print(f' {c} Celcius = {round(f,2)} Fahrenheit')'''

#Task 9 Endirimli corek
'''kohnecorek = int(input('Number of loaves: '))
adi = kohnecorek * 3.49
endirim = adi - kohnecorek * 1.396
print(f' Total price: {round(adi, 2)} dollars')
print(f' Discount: {round(endirim, 2)} dollars')'''
