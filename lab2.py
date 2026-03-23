#1 verilen iki ededden boyuk olani cap eden proqram
'''a = int(input('Birinci ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
if a > b:
    print(f' Boyuk olan eded --> {a}')
else:
    if a < b:
        print(f' Boyuk olan eded --> {b}')
    else:
        print(' Daxil edilen ededler bir-birine beraberdir.')'''

#2 verilen ededin isaresini yoxlayan proqram
'''a = float(input('Ededi daxil edin: '))
if a > 0:
    print('Ededin isaresi musbetdir.')
else:
    if a == 0:
        print('Eded 0-dir.')
    else:
        print('Ededin isaresi menfidir.')'''

#3 Tələbənin adını və 3 qiymət daxil etməklə, onun adını, qiymətlərinin ədədi ortasını və orta qiymətinə uyğun gələn nəticəni çap edən proqram
'''name = input('Telebenin adini daxil edin: ')
a = float(input('Birinci qiymeti daxil edin: '))
b = float(input('Ikinci qiymeti daxil edin: '))
c = float(input('Ucuncu qiymeti daxil edin: '))
ededi_orta = (a + b + c) // 3
print(f' Telebenin adi: {name}, ortalama qiymeti = {ededi_orta}', end=' ')
if ededi_orta >= 85:
    print('Excellent')
elif ededi_orta >= 75 and ededi_orta < 85:
    print('Very Good')
elif ededi_orta >= 65 and ededi_orta < 75:
    print('Good')
elif ededi_orta >= 50 and ededi_orta < 65:
    print('Pass')
else:
    print('Fail')'''

#4 ededin 3-e bolunmesini yoxlayan proqram
'''a = int(input('Ededi daxil edin: '))
if a % 3 == 0:
    print('Eded 3-e bolunur.')
else:
    print('Eded 3-e bolunmur.')'''

#5 ededin 6-a bolunmesini yoxlayan proqram
'''a = int(input('Ededi daxil edin: '))
if a % 6 == 0:
    print('Eded 6-a bolunur.')
else:
    print('Eded 6-a bolunmur.')'''

#6 ededin cut olmasini yoxlayan proqram
'''a = int(input('Ededi daxil edin: '))
if a % 2 == 0:
    print('Eded cutdur.')
else:
    print('Eded tekdir.')'''

#7 İstifadəçi tərəfindən daxil olunan 3 ədədin cəmi tapılmalıdır, nəzərə alınmalıdır  ki, əgər bütün ədədlər eynidirsə, cəmin 3 mislini ekranda gosteren proqram
'''a = int(input('Birinci ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
c = int(input('Ucuncu ededi daxil edin: '))
cem = a + b + c
if a == b and b == c:
    print(cem * 3)
else:
    print(cem)'''

#8 İstifadəçi tərəfindən daxil olunan 3 ədədin cəmi tapılmalıdır, nəzərə alınmalıdır ki, əgər hər hansı 2 ədəd eynidirsə, cəmi sıfır olaraq ekranda gosteren proqram
'''a = int(input('Birinci ededi daxil edin: '))
b = int(input('Ikinci ededi daxil edin: '))
c = int(input('Ucuncu ededi daxil edin: '))
cem = a + b + c
if a == b or b == c or a == c:
    print('0')
else:
    print(cem)'''

#9 Kvadrat tənliyi həll edən proqramı yazın. Diskriminanta əsasən tənliyin neçə kökü olduğunu və onların nəyə bərabər olduğunu ekrana çıxarsın, kökü olmadığıni gosteren proqram
'''a = float(input('a-ni daxil edin: '))
b = float(input('b-ni daxil edin: '))
c = float(input('c-ni daxil edin: '))
print(f' Tenlik: {int(a)}x^2 + {int(b)}x + {int(c)}')
D = (b ** 2) - (4 * a * c)
print(f' Diskriminant = {D}')
if D > 0:
    print(' Tenliyin 2 muxtelif koku var: ', end=' ')
    x1 = ((-1 * b) - (D ** 0.5)) / (2 * a)
    x2 = ((-1 * b) + (D ** 0.5)) / (2 * a)
    print(f'x1 = {x1} ve x2 = {x2}')
else:
    if D == 0:
        print(' Tenliyin 1 koku var: ', end=' ')
        x = (-1 * b) / (2 * a)
        print(f'x = {x}')
    else:
        print(' Tenliyin heqiqi koku yoxdur.')'''

#10 Endirim tətbiq olunmuş məhsulun qiymətini hesablayan proqramı yazın. Əgər məhsulun qiyməti 1000 manatdan artıqdırsa, 10% endirim tətbiq eden proqram
'''qiymet = int(input('Mehsulun qiymetini daxil edin: '))
if qiymet >= 1000:
    qiymet = qiymet - (qiymet / 100)
    print(f' Endirimle qiymet = {qiymet}')
else:
    print(f' Endirim yoxdur. Qiymet = {qiymet}')'''

#11 Endirim tətbiq olunmuş məhsulun qiymətini hesablayan proqramı yazın. Əgər məhsulun qiyməti 500 manatdan artıqdırsa – 3%, 1000 manatdan artıqdırsa – 5% endirim tətbiq eden proqram
'''qiymet = int(input('Mehsulun qiymetini daxil edin: '))
if qiymet >= 500 and qiymet < 1000:
    print(f' 3% endirim tetbiq edilir: Yeni qiymet = {qiymet - (qiymet * 3 / 100)}')
elif qiymet >= 1000:
    print(f' 5% endirim tetbiq edilir: Yeni qiymet = {qiymet - (qiymet * 5 / 100)}')
else:
    print(f' Endirim yoxdur. Qiymet = {qiymet}')'''

#12 muqayiseni gosteren proqram
'''a = float(input('Birinci ededi daxil edin: '))
b = float(input('Ikinci ededi daxil edin: '))
if a > b:
    print(f' Muqayise: {a} > {b}')
else:
    if a < b:
        print(f' Muqayise: {a} < {b}')
    else:
        print(f' Muqayise: {a} = {b}')'''

#13 [0, 100] aralığında təsadüfi 3 ədədin medianını tapan proqram
'''from random import randint
a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
print(a, b, c)
if a > b and a < c:
    median = a
elif b > a and b < c:
    median = b
else:
    median = c
print(f' Median = {median}')'''

#14 Tərəflərinin sayına görə fiqurun adını müəyyənləşdirən proqram
'''#1ci versiya
a = int(input('Tereflerin sayini daxil edin: '))
if a >= 3 and a <= 10:
    if a == 3:
        print(' Triangle')
    elif a == 4:
        print(' Quadrilateral')
    elif a == 5:
        print(' Pentagon')
    elif a == 6:
        print(' Hexagon')
    elif a == 7:
        print(' Heptagon')
    elif a == 8:
        print(' Octagon')
    elif a == 9:
        print(' Nonagon')
    else:
        print(' Decagon')
else:
    print(' Xeta! Teref sayini 3 - 10 araliginda daxil edin.')

#2ci versiya
a = int(input('Tereflerin sayini daxil edin: '))
fiqurlar = ['Triangle', 'Quadrilateral', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Decagon']
k = 0
if a >= 3 and a <= 10:
    for i in range(3, 11):
        if i == a:
            print(f' Fiqurun adi --> {fiqurlar[k]}')
        k += 1
else:
    print(' Xeta! Teref sayini 3 - 10 araliginda daxil edin.')'''

#15 istifadəçi tərəfindən string kimi daxil edilmiş ayın adına əsasən onun günlərin sayını ekrana çıxaran proqram
'''ay = input('Ayin adini daxil edin: ')
if ay == 'fevral' or ay == 'Fevral':
    il = int(input('Ili daxil edin: '))
    if il % 4 == 0:
        print(' Bu il Fevral ayi 29 gundur.')
    else:
        print(' Bu il Fevral ayi 28 gundur.')
elif ay == 'yanvar' or ay == 'mart' or ay == 'may' or ay == 'iyul' or ay == 'avqust' or ay == 'oktyabr' or ay == 'dekabr' or ay == 'Yanvar' or ay == 'Mart' or ay == 'May' or ay == 'Iyul' or ay == 'Avqust' or ay == 'Oktyabr' or ay == 'Dekabr':
    print(f' {ay} ayi 31 gundur.')
elif ay == 'aprel' or ay == 'iyun' or ay == 'sentyabr' or ay == 'noyabr' or ay == 'Aprel' or ay == 'Iyun' or ay == 'Sentyabr' or ay == 'Noyabr':
    print(f' {ay} ayi 30 gundur.')
else:
    print('Bele ay teqvimde yoxdur')'''

#16 Asif Vasif Agasifin yaslarini muqayise eden proqram
'''asif = int(input('Asifin yasini daxil edin: '))
vasif = int(input('Vasifin yasini daxil edin: '))
agasif = int(input('Agasifin yasini daxil edin: '))
print(f' Asifin yasi: {asif}')
print(f' Vasifin yasi: {vasif}')
print(f' Agasifin yasi: {agasif}')
if asif > vasif and asif > agasif:
    print(' Cavab: Asif hamidan yasca boyukdur.')
elif vasif > asif and vasif > agasif:
    print(' Cavab: Vasif hamidan yasca boyukdur.')
elif agasif > asif and vasif < agasif:
    print(' Cavab: Agasif hamidan yasca boyukdur.')
elif vasif == asif and vasif > agasif:
    print(' Cavab: Vasif ve Asif Agasifden yasca boyukdur.')
elif vasif == agasif and vasif > asif:
    print(' Cavab: Vasif ve Agasif Asifden yasca boyukdur.')
elif agasif == asif and vasif < agasif:
    print(' Cavab: Agasif ve Asif Vasifden yasca boyukdur.')
else:
    print(' Cavab: Hamisi eyni yasdadirlar.')'''

#17 terefine gore ucbucagin novunu teyin eden proqram
'''def ucbucaq(a, b, c):
    if a < (b + c) and a > abs(b - c):
        return True
    return False
a = int(input('Birinci terefin uzunlugunu daxil edin: '))
b = int(input('Ikinci terefin uzunlugunu daxil edin: '))
c = int(input('Ucuncu terefin uzunlugunu daxil edin: '))
if ucbucaq(a, b, c) == True and a > 0 and b > 0 and c > 0:
    print(f' Ucbucagin terefleri: {a}, {b}, {c}-dir.')
    if a == b and b == c:
        print(' Bu beraberterefli ucbucaqdir.')
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        print(' Bu beraberyanli ucbucaqdir.')
    else:
        print(' Bu muxtelifterefli ucbucaqdir.')
else:
    print(' Bele ucbucaq movcud deyil!')'''

#18 ses desibeline gore sesin adini cixaran proqram
'''dB = int(input('Ses seviyyesini desibel ile daxil edin: '))
if dB >= 40 and dB <= 130:
    print(f' Ses seviyyesi = {dB}dB')
    if dB == 40:
        print(f' {dB}dB-e uygun gelen ses -> Quiet room-dur')
    elif dB == 70:
        print(f' {dB}dB-e uygun gelen ses -> Alarm clock-dur')
    elif dB == 106:
        print(f' {dB}dB-e uygun gelen ses -> Gas lawnmower-dir')
    elif dB == 130:
        print(f' {dB}dB-e uygun gelen ses -> Jackhammer-dir')
    elif dB > 40 and dB < 70:
        print(f' {dB}dB-e uygun gelen ses -> Quiet room ve Alarm clock araligindadir.')
    elif dB > 70 and dB < 106:
        print(f' {dB}dB-e uygun gelen ses -> Alarm clock ve Gas lawnmower araligindadir.')
    elif dB > 106 and dB < 130:
        print(f' {dB}dB-e uygun gelen ses -> Gas lawnmower ve Jackhammer araligindadir.')
else:
    print(' Ses seviyyesini 40dB-130dB araliginda daxil edin.')'''

#19 daxil edilen ilin uzun il olub olmamasini yoxlayan proqram
'''il = int(input('Ili daxil edin: '))
if (il % 100 != 0) and (il % 400 == 0 or il % 4 == 0):
    print(f' {il} uzun ildir, hemin il 366 gun olmusdur.')
else:
    print(f' {il} uzun il deyildir.')'''

#20 daxil edilen qiymete esasen zelzelenin miqyasini gosteren proqram
'''rixter = float(input('Zelzelenin balini qeyd edin: '))
print(f' Zelzelenin bali: {rixter}-dir.')
if rixter < 2.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Microdur.') 
elif rixter >= 2.0 and rixter < 3.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Very minordur.')
elif rixter >= 3.0 and rixter < 4.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Minordur.')
elif rixter >= 4.0 and rixter < 5.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Lightdir.')
elif rixter >= 5.0 and rixter < 6.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Moderatedir.')
elif rixter >= 6.0 and rixter < 7.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Strongdur.')
elif rixter >= 7.0 and rixter < 8.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Majordur.')
elif rixter >= 8.0 and rixter < 10.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Greatdir.')
elif rixter >= 10.0:
    print(f' Rixter skalasina esasen {rixter} balli zelzele Meteoricdir.')'''

#21 daxil edilen sahmat xanasinin ag yoxsa qara oldugunu gosteren proqram
'''herfler = 'abcdefgh'
reqemler = '12345678'
herf = input('Xananin herf unvanini yazin: ')
reqem = int(input('Xananin reqem unvanini yazin: '))
if herf in herfler and str(reqem) in reqemler:
    print(f' Daxil edilen xana {herf}{reqem}')
    if ((reqem == 2 or reqem == 4 or reqem == 6 or reqem == 8) and (herf == 'a' or herf == 'c' or herf == 'e' or herf == 'g')) or ((reqem == 1 or reqem == 3 or reqem == 5 or reqem == 7) and (herf == 'b' or herf == 'd' or herf == 'f' or herf == 'h')):
        print(' Bu xana ag rengdedir')
    else:
        print(' Bu xana qara rengdedir')
else:
    print(' Sahmat taxtasinda bele bir xana movcud deyil.')'''

#22 noqtenin oblasta daxil olub olmamasini yoxlayan proqram
'''#A
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if y >= ((x ** 2) - 2) and (y <= x or y >= (-1 * x)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#B
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (((x ** 2) + (y ** 2)) <= 1) and (y > x or (y < 0 and x < 0)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#C 
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (((x ** 2) + (y ** 2)) <= 1) and ((y >= x and y >= (-1 * x)) or (y <= x and y <= (-1 * x)) or y <= x):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#D
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if ((y >= (2 * x ** 2)) and (y >= (1 - x)) and (x <= 1)) or ((y <= (2 * x ** 2)) and (y >= (1 - x)) and (x <= 1) and (x > 0)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#E
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (x >= 0) and ((x ** 2 + y ** 2) <= 1) or ((y <= 1) and (y >= (x - 1))):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#F
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if ((x ** 2 + y ** 2) <= 1) or ((x >= 0 and y >= 0) and (x <= 1 and y <= 1)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#G
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if x != 0:
    if ((y >= (1 / x)) and (x >= 0) and (y <= (-1 * x) + 4)) or ((y <= 1 / x) and (x <= 0) and (y >= (-1 * x) - 4)):
        print(f' ({x};{y}) noqtesi bu saheye daxildir.')
    else:
        print(' Noqte buraya aid deyil.')
else:
    print(' Mexrec 0 ola bilmez.')'''

'''#H
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if ((y >= (x ** 2)) and (y <= 1)) or ((y <= ((-1 * x) ** 2)) and (y >= -1)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#J
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (((x ** 2 + y ** 2) >= 4) and (x <= 0) and (y <= 0) and (x >= y) and (y >= -2)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#K
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (y >= ((x - 2) ** 2) - 3) and ((x >= abs(y)) and (y >= 0)) or ((x <= abs(y)) and (y <= 0)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#L
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (((x ** 2 + y ** 2) <= 25) and (x <= 0)) and ((y >= (x + 2)) or (y <= 0)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#M
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if ((x ** 2 + y ** 2) <= 1) and (((x <= 0) and (y >= 0)) or ((x >= 0) and (y <= 0)) or ((x >= 0) and (y >= 0) and (y <= (1 - x)))):            
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''

'''#N
x = float(input('X koordinatini daxil edin: '))
y = float(input('Y koordinatini daxil edin: '))
if (((x ** 2 + y ** 2) <= 1) and (y >= x)) or ((x >= -1) and (y <= 1) and (x <= 0) and (y >= 0)):
    print(f' ({x};{y}) noqtesi bu saheye daxildir.')
else:
    print(' Noqte buraya aid deyil.')'''



    
