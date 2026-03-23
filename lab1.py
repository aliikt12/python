#1 a=2^4 hesablayan proqram
'''a = 2 ** 4
print(a)'''

#2 eni, uzunlugu alib duzbucaqli sahesini hesablayan proqram
'''a = float(input('Eni daxil edin: '))
b = float(input('Uzunlugu daxil edin: '))
S = a * b
print(f' S = {S}')'''

#3 verilenleri daxil edib paralelipipedin hecmi, sethinin sahesini hesablayan proqram
'''a = float(input('Paralelipipedin enini daxil edin: '))
b = float(input('Paralelipipedin uzulugunu daxil edin: '))
c = float(input('Paralelipipedin hundurluyunu daxil edin: '))
V = a * b * c
S = 2 * (a * b + a * c + b * c)
print(f' V = {V}, S = {S}')'''

#4 silindrin hecmini hesablayan proqram
'''from math import pi
r = float(input('Silindrin radiusunu daxil edin: '))
h = float(input('Silindrin hundurluyunu daxil edin: '))
V = pi * (r ** 2) * h
print(f' V = {V}')'''

#5 ucbucagin iki terefi ve aralarindaki bucaga esasen sahesini hesablayan proqram
'''from math import sin, pi
a = float(input('Birinci terefi daxil edin: '))
b = float(input('Ikinci terefi daxil edin: '))
degrees = float(input('Verilen iki teref arasinda bucagi daxil edin: '))
radians = (degrees * pi) / 180
S = (a * b * sin(radians)) / 2
print(f' S = {S}')'''

#6 daxil edilen 3 tam ededin cemi hasili ve ededi ortasini tapan proqram
'''a = int(input('Birinci ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
c = int(input('Ucuncu ededi daxil edin: '))
cem = a + b + c
hasil = a * b * c
ededi_orta = cem / 3
print(f' cem = {cem}, hasil = {hasil}, ededi orta = {ededi_orta}')'''

#7 tesadufi verilen 4 reqemli ededin reqemlerinin kvadratlari cemi ve hasilini cixaran proqram
'''from random import randint
a = randint(1000,9999)
print(f' eded = {a}')
last = a % 10
third = a // 10 % 10
second = a // 100 % 10
first = a // 1000
cem = (first ** 2) + (second ** 2) + (third ** 2) + (last ** 2)
hasil = first * second * third * last
print(f' kvadratlar cemi = {cem}, reqemler hasili = {hasil}')'''

#8 [6.5; 10.5] intervalındakı təsadüfi iki ədədin hasilini tapan proqram
'''from random import uniform
a = uniform(6.5, 10.5)
b = uniform(6.5, 10.5)
print(f' a = {a}, b = {b}')
hasil = a * b
print(f' a * b = {round(hasil, 2)}')'''

#9 Təsadüfi seçilmiş beşrəqəmli ədədin rəqəmlərini və qarşısında kvadratlarını alt-alta ekrana çıxaran proqram 
'''from random import randint
a = randint(10000, 99999)
print(f' a = {a}')
last = a % 10
fourth = a // 10 % 10
third = a // 100 % 10
second = a // 1000 % 10
first = a // 10000 % 10
print(f' 1. {first} --> {first**2}')
print(f' 2. {second} --> {second**2}')
print(f' 3. {third} --> {third**2}')
print(f' 4. {fourth} --> {fourth**2}')
print(f' 5. {last} --> {last**2}')'''

#10 x və y [-1,1] intervalında təsadüfi həqiqi ədədlərdir. Verilmiş düstura əsasən a və b-nın  qiymətini vergüldən sonra 3 rəqəm saxlamaqla tapan proqram
'''from random import uniform
from math import sin, cos
x = uniform(-1, 1)
y = uniform(-1, 1)
print(f' x = {x}, y = {y}')
a = ((1 + (y ** 2)) ** 0.5) * sin((x ** 2) / (1 + abs(y)))
b = cos((sin(5 * x) ** 2) / ((abs(y)) ** 0.5))
print(f' a = {round(a,3)}, b = {round(b,3)}')'''

#11 daxil edilen 3reqemli ededin reqemlerini , ile ayiran proqram
'''a = int(input('Ucreqemli eded daxil edin: '))
last = a % 10
second = a // 10 % 10
first = a // 100
print(f' {first}, {second}, {last}')'''
