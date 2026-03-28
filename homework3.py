#Homework 3
#Movzu: while, for
#Task 1 Temperatur
'''print('Celsius         Fahrenheit')
def fahrenheit(a):
    f = a * 1.8 + 32
    return f
for i in range(0, 101, 10):
    if i == 0:
        print(f'{i}               {int(fahrenheit(i))}')
    elif i == 100:
        print(f'{i}             {int(fahrenheit(i))}')
    else:
        print(f'{i}              {int(fahrenheit(i))}')'''

#Task 2 Ededi orta
'''N = int(input('Max number to compute the average value: '))
cem = 0
if N > 0:
    for i in range(1, N + 1):
        a = int(input(f'Value {i}: '))
        cem += a
    print(f' Average value: {cem / N}')
else:
    print(' Error message')'''

#Task 3 Orta bal
'''i = 0
cem = 0
while True:
    a = input("Enter the grade('end' to quit): ")
    if a == 'end':
        break
    i += 1
    if a == 'A' or a == 'A+':
        cem += 4
    elif a == 'A-':
        cem += 3.7
    elif a == 'B+':
        cem += 3.3
    elif a == 'B':
        cem += 3
    elif a == 'B-':
        cem += 2.7
    elif a == 'C+':
        cem += 2.3
    elif a == 'C':
        cem += 2
    elif a == 'C-':
        cem += 1.7
    elif a == 'D+':
        cem += 1.3
    elif a == 'D':
        cem += 1
    elif a == 'F':
        cem += 0
print(f' A grade point average: {cem / i}')'''

#Task 4 Giris qiymeti
'''total = 0
while True:
    a = input("Enter the age of the guest ('end' to quit): ")
    if a == 'end':
        break
    if int(a) >= 3 and int(a) <= 12:
        total += 14
    elif int(a) >= 65:
        total += 18
    elif int(a) <= 2:
        total += 0
    else:
        total += 23
print(f' The total for that group is ${round(float(total), 2)}')'''

#Task 5 Coxbucaqlinin perimetri
'''x = int(input('Enter the x part of the coordinate: '))
length1 = 0
xcopy = x
y = int(input('Enter the y part of the coordinate: '))
ycopy = y
perimeter = 0
while True:
    x1 = input("Enter the x part of the coordinate ('end' to quit): ")
    if x1 == 'end':
        break
    y1 = input("Enter the y part of the coordinate: ")
    length = (((int(x1) - int(x)) ** 2) + ((int(y1) - int(y)) ** 2)) ** 0.5
    length1 = (((int(x1) - int(xcopy)) ** 2) + ((int(y1) - int(ycopy)) ** 2)) ** 0.5
    perimeter += length
    x = x1
    y = y1
print(f' The perimeter of that polygon is {round(perimeter + length1, 2)}')'''
