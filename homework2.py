#Homework 2
#Movzu: if, nested if
#Task 1 Sait ve ya samit
'''herf = input('Enter a letter of the alphabet: ')
if herf == 'a' or herf == 'e' or herf == 'i' or herf == 'o' or herf == 'u':
    print(' Entered alphabet is a vowel!')
elif herf == 'y':
    print(' Sometimes it is a vowel, and sometimes it is a consonant!')
else:
    print(' Entered alphabet is a consonant!')'''

#Task 2 Movsum
'''ay = input('Enter name of the month [ex. June]: ')
gun = int(input('Enter the day [ex. 5]: '))
print(f' {ay} {gun} is in', end = ' ')
if (ay == 'March' and gun >= 20) or ay == 'April' or ay == 'May' or (ay == 'June' and gun < 21):
    print('Spring')
elif (ay == 'June' and gun >= 21) or ay == 'July' or ay == 'August' or (ay == 'September' and gun < 22):
    print('Summer')
elif (ay == 'September' and gun >= 22) or ay == 'October' or ay == 'November' or (ay == 'December' and gun < 21):
    print('Fall')
else:
    print('Winter')'''

#Task 3 Gorunen isigin dalga uzunlugu
'''wave = float(input('Enter the wavelenght in nm: '))
if wave < 380 or wave > 750:
    print(' Invalid input!')
else:
    if wave >= 380 and wave < 450:
        print(' The relevant color is Violet!')
    elif wave >= 450 and wave < 495:
        print(' The relevant color is Blue!')
    elif wave >= 495 and wave < 570:
        print(' The relevant color is Green!')
    elif wave >= 570 and wave < 590:
        print(' The relevant color is Yellow!')
    elif wave >= 590 and wave < 620:
        print(' The relevant color is Orange!')
    else:
        print(' The relevant color is Red!')'''

#Task 4 Cin burcu
'''year = int(input('Enter the year [ex. 2021]: '))
if year < 0:
    print(' Invalid year!')
else:
    print(f' {year} is the year of the', end = ' ')
    if year % 12 == 0:
        print('Monkey')
    elif year % 12 == 1:
        print('Rooster')
    elif year % 12 == 2:
        print('Dog')
    elif year % 12 == 3:
        print('Pig')
    elif year % 12 == 4:
        print('Rat')
    elif year % 12 == 5:
        print('Ox')
    elif year % 12 == 6:
        print('Tiger')
    elif year % 12 == 7:
        print('Hare')
    elif year % 12 == 8:
        print('Dragon')
    elif year % 12 == 9:
        print('Snake')
    elif year % 12 == 10:
        print('Horse')
    else:
        print('Sheep')'''

#Task 5 Burcun teyin edilmesi
'''ay = input('Enter a month [ex. March]: ')
gun = int(input('Enter the day [ex. 12]: '))
if gun > 31:
    print(' Either a month or a day is invalid!')
else:
    print(' Your zodiac sign is', end = ' ')
    if (ay == 'December' and gun >= 22) or (ay == 'January' and gun <= 19):
        print('Capricorn')
    elif (ay == 'January' and gun >= 20) or (ay == 'Febuary' and gun <= 18):
        print('Aquarius')
    elif (ay == 'Febuary' and gun >= 19) or (ay == 'March' and gun <= 20):
        print('Pisces')
    elif (ay == 'March' and gun >= 21) or (ay == 'April' and gun <= 19):
        print('Aries')
    elif (ay == 'April' and gun >= 20) or (ay == 'May' and gun <= 20):
        print('Taurus')
    elif (ay == 'May' and gun >= 21) or (ay == 'June' and gun <= 20):
        print('Gemini')
    elif (ay == 'June' and gun >= 21) or (ay == 'July' and gun <= 22):
        print('Cancer')
    elif (ay == 'July' and gun >= 23) or (ay == 'August' and gun <= 22):
        print('Leo')
    elif (ay == 'August' and gun >= 23) or (ay == 'September' and gun <= 22):
        print('Virgo')
    elif (ay == 'September' and gun >= 23) or (ay == 'October' and gun <= 22):
        print('Libra')
    elif (ay == 'October 23' and gun >= 23) or (ay == 'November' and gun <= 21):
        print('Scorpio')
    else:
        print('Sagittarius')'''

#Task 6 Oblasta dusen noqte
'''x = float(input('Enter x: '))
y = float(input('Enter y: '))
if ((x ** 2) + (y ** 2) >= 4) and (y <= x) and (x <= 2) and (y >= 0):
    print(' The point is in the shaded area')
else:
    print(' The point is not in the shaded area')'''

#Task 7 Oblasta dusen noqte
'''x = float(input('Enter x: '))
y = float(input('Enter y: '))
if (y >= ((x - 2) ** 2) - 3) and ((x >= abs(y) and y >= 0) or (x <= abs(y) and y <= 0)):
    print(' The point is in the shaded area')
else:
    print(' The point is not in the shaded area')'''

#Task 8 Oblasta dusen noqte
'''x = float(input('Enter x: '))
y = float(input('Enter y: '))
if y <= (x ** 2) and ((y >= (2 - x) and (x <= 0)) or (y <= (2 - x) and x >= 0 and y >= 0)):
    print(' The point is in the shaded area')
else:
    print(' The point is not in the shaded area')'''

#Task 9 Oblasta dusen noqte
'''x = float(input('Enter x '))
y = float(input('Enter y: '))
if (((x ** 2) + (y ** 2) <= 1) and (y <= 0) and (y >= x)) or ((x ** 2) + (y ** 2) <= 1 and (y <= 0) and (y <= x) and (y >= -x)) or ((x ** 2) + (y ** 2) >= 1 and (y <= 0) and (y <= x) and (y <= -x)) or ((x ** 2) + (y ** 2) <= 1 and (y >= 0) and (y >= x) and (y >= -x)):
    print(' The point is in the shaded area')
else:
    print(' The point is not in the shaded area')'''

#Task 10 Oblasta dusen noqte
'''x = float(input('Enter x: '))
y = float(input('Enter y: '))
if ((y >= x ** 2) and (y >= (4 - x ** 2)) and (x >= 0)) or ((y <= x ** 2) and (y >= (2 - x)) and (x <= 0)) or ((y <= (4 - x ** 2)) and (y >= x ** 2) and (y <= (2 - x)) and (x <= 0)) or ((y <= (4 - x ** 2)) and (y <= (2 - x)) and (x >= 0) and (y >= 0) and (y <= x ** 2)):
    print(' The point is in the shaded area')
else:
    print(' The point is not in the shaded area')'''
