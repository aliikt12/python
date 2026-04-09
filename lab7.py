#1 Aşağıdakı tuple-da verilmiş 24 ədədinin indekslərini çap eden proqram
'''Tuple = (4, 6, 3, 9, 12, 24, 24, 76, 63)
print(' 24 ededinin indeksi: ', end = '')
for i in range(len(Tuple)):
    if Tuple[i] == 24:
        print(i, end = ' ')'''

#2 Aşağıdakı tuple-da verilmiş ədədlərdən 3-ə bölünən ədədləri çap eden proqram
'''Tuple = (4, 6, 3, 9, 12, 24, 24, 76, 63)
print(' 3-e bolunen ededler: ', end = '')
for i in Tuple:
    if i % 3 == 0:
        print(i, end = ' ')'''

#3 İstifadəçi tərəfindən 5 ədəd daxil edilərək list yaradın. Listin hər bir ədədini 5 vahid artıraraq yeni liste elave eden proqram
'''a = [int(input(f'{i}. ')) for i in range(1,6)]
print(f' List1 = {a}')
for i in range(len(a)):
    a[i] += 5
print(f' List2 = {a}')'''

#4 Istifadəçi tərəfindən 5 ədəd daxil edilərək list yaradın. Listin tərkibindəki cüt ədədləri listdən çıxarmaqla qalan elementləri yeni listə yığıb, çap edən proqram
'''a = [int(input(f'{i}. ')) for i in range(1,6)]
b = []
print(f' List1 = {a}')
for i in range(len(a)):
    if a[i] % 2 == 1:
        b += [a[i]]
print(f' List2 = {b}')'''

#5 Listi [0, 10] intervalı arasında təsadüfi ədədlərlə doldurun (ədədlərin sayı = 7) və bütün elementlərin a) cəmini, b) hasilini, c) ədədi ortasını, d) ən böyüyünü və onun indeksini, e) ən kiçiyini və ounu indeksini tapan proqram 
'''from random import randint
a = [randint(0, 10) for i in range(7)]
print(f'List = {a}')
cem = 0
hasil = 1
maxx = float('-inf')
minn = float('inf')
for i in range(len(a)):
    cem += a[i]
    hasil *= a[i]
    if maxx < a[i]:
        maxx = a[i]
        yermax = i
    if minn > a[i]:
        minn = a[i]
        yermin = i
print(f' Cem = {cem}  Hasil = {hasil}  Ededi orta = {round(cem / 7, 2)}')
print(f' En boyuk eded = {maxx} , indeks = {yermax}')
print(f' En kicik eded = {minn} , indeks = {yermin}')'''

#6 Massivi [0, 100] intervalında olan təsadüfi ədədlərlə doldurun (ədədlərin sayı = 10). 50-dən kiçik olan və 50-dən böyük bərabər olan elementlərinin ədədi ortasını çap edən proqram
'''from random import randint
a = [randint(0, 100) for i in range(10)]
print(a)
cem1 = 0
say1 = 0
cem2 = 0
say2 = 0
for i in a:
    if i < 50:
        cem1 += i
        say1 += 1
    else:
        cem2 += i
        say2 += 1
print(f' [0, 50) araliginda ededi orta = {cem1 / say1}')
print(f' [50, 100) araliginda ededi orta = {cem2 / say2}')'''

#7 1 ilə 15 arasında olan ədədlərin kvadratlarından təşkil olunmuş listdə ilk 5 və son 5 elementləri çapedən proqram
'''a = [i ** 2 for i in range(1, 16)]
print(f'List = {a}')
print(f' Ilk 5 element = ', end = '')
print(*a[0:5])
print(f' Son 5 element = ', end = '')
print(*a[-5::])'''

#8 Verilmiş iki listin ortaq elementi varsa True, yoxdursa False nəticəsi verən funksiya
'''def funksiya(a, b):
    flag = 0
    for i in a:
        if i in b:
            print(' Cavab: ortaq element var.')
            flag = 1
    if flag == 0:
        print(' Cavab: ortaq element yoxdur.')
from random import randint
list1 = [randint(0, 10) for i in range(3)]
list2 = [randint(0, 10) for i in range(3)]
print(f'List1 = {list1}')
print(f'List2 = {list2}')
funksiya(list1, list2)'''

#9 2 listdə eyni indeksdə yerləşən eyni elementləri və onların sayını ekrana çıxaran proqram
'''from random import randint
list1 = [randint(0, 10) for i in range(5)]
list2 = [randint(0, 10) for i in range(5)]
print(f'List1 = {list1}')
print(f'List2 = {list2}')
count = 0
eyni = []
for i in range(len(list1)):
    if list1[i]  == list2[i]:
        count += 1
        eyni += [list1[i]]
print(f' Tekrarlanan elementler: ', end = '')
print(*eyni)
print(f' Eyni indeksde yerleshen eyni elementlerin sayi = {count}')'''

#10 Listdəki hər elementi bir pozisiya sola sürüşdürün və beləcə ilk elementi isə sonuncu pozisiyada saxlayan proqram
'''from random import randint
list1 = [randint(0, 100) for i in range(5)]
print(f'List1 = {list1}', end = '   ')
list2 = list1[1:5] + [list1[0]]
print(f'List2 = {list2}')'''

#11 Verilmiş 2 listin uyğun indeksli elemenlerini cütləşdirib 3-cü yeni listə yazan proqram
'''List1 = [input(f'{i}. ') for i in range(1,4)] 
List2 = [int(input(f'{i}. ')) for i in range(1,4)]
print(f'List1 = {List1}')
print(f'List2 = {List2}')
yeni = []
for i in range(3):
    yeni += [[List1[i]] + [List2[i]]]
print(f' Yeni_list = {yeni}')'''

#12 Listin ilk cüt ədədinə rastlayana qədər bütün tək ədədlərin cəmini tapan proqram
'''from random import randint
list1 = [randint(0, 10) for i in range(11)]
cem = 0
print(f'List = {list1}')
for i in list1:
    if i % 2 == 1:
        cem += i
    else:
        break
print(f' Listin ilk cut ededine qeder olan cem: {cem}')'''

#13 N ölçülü listin içərisini [10, 50] intervalında təsadüfi ədədlərlə doldurun. Həmin ədədlərdən müəyyən ədədin kvadratı olan ədədləri başqa listə köçüren proqram
'''from random import randint
n = int(input('Listin olcusu N: '))
list1 = [randint(10, 50) for i in range(n)]
list2 = []
print(f'List1 = {list1}')
for i in list1:
    if (i ** 0.5) % 1 == 0:
        list2 += [i]
print(f' List2 = {list2}')'''

#14 N ölçülü listin içərisini [100, 999] aralığında təsadüfi ədədlərlə doldurun. Ədədlərin sayı istifadəçi tərəfindən daxil edilir. Listin içərisində son iki rəqəminin modul fərqi və cəmi tək olan ədədləri başqa listə yığan proqram
'''from random import randint
n = int(input('Ededlerin sayi N: '))
list1 = [randint(100, 999) for i in range(n)]
print(f'List1 = {list1}')
yekun = []
for i in list1:
    if abs((i % 10) - (i // 10 % 10)) % 2 == 1 and ((i % 10) + (i // 10 % 10)) % 2 == 1:
        yekun += [i]
print(f' List2 = {yekun}')'''

#15 Massivi [0, 100] intervalı arasında olan təsadüfi ədədlərlə doldurun. Ədədlərin sayı istifadəçi tərəfindən daxil edilir. Həmin massivdən sadə ədədləri seçib digər massivə köçüren proqram
'''from random import randint
n = int(input('Ededlerin sayi N: '))
list1 = [randint(0, 100) for i in range(n)]
print(f'A = {list1}', end = '')
yekun = []
def sade(a):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0 and a != 1:
        return True
    return False
for i in list1:
    if sade(i):
        yekun += [i]
print(f'  B = {yekun}')'''

#16 Massivi [-10, 10] parçasında dəyişən təsadüfi ədədlərlə doldurun (ədədlərin sayı = 10) və həmin massivdən cüt və mənfi ədədləri seçib digər massivə köçüren proqram
'''from random import randint
list1 = [randint(-10, 10) for i in range(10)]
b = []
print(f'A = {list1}')
for i in list1:
    if i < 0 and abs(i) % 2 ==0:
        b += [i]
print(f' B = {b}')'''

#17 Mənfi olmayan tam ədədləri massivdən çıxarıb yeni massivə əlavə eden proqram
'''List1 = [1, 2, 'aasf', '1', '123', 123]
print(f'List1 = {List1}')
yekun = []
for i in List1:
    if type(i) == int and i > 0:
        yekun += [i]
print(f' List2 = {yekun}')'''

#18 İstifadəçi tərəfindən daxil edilən müsbət tam ədədin bütün uyğun bölənlərini bir listə yığıb çap edən proqram
'''a = int(input('Musbet tam eded: '))
yekun = []
for i in range(1, a + 1):
    if a % i == 0:
        yekun += [i]
print(f' List = {yekun}')'''

#19 N-in hər bir qiyməti üçün silsilənin hədlərindən ibarət olan list yaradan proqram
'''#duz versiya
from math import sin, log
N = [6, 2, 5, 3, 9, 7, 4]
print(f'N = {N}')
yekun = []
for i in N:
    cavab = 0
    for j in range(1, i + 1):
        cavab += (4 * sin(j) + 2 * j) / (log(9 * j, 3) * 2 ** j)
    yekun += [round(cavab, 2)]
print(f' List = {yekun}')

#tapsiriqda verilen
from math import sin, log
N = [6, 2, 5, 3, 9, 7, 4]
print(f'N = {N}')
yekun = []
cavab = 0
for i in N:
    for j in range(1, i + 1):
        cavab += (4 * sin(j) + 2 * j) / (log(9 * j, 3) * 2 ** j)
    yekun += [round(cavab, 2)]
print(f' List = {yekun}')'''

#20 N-in hər bir qiyməti üçün silsilənin hədlərindən ibarət olan list yaradan proqram
'''#duz versiya
from math import cos, log
N = [6, 2, 5, 3, 9, 7, 4]
print(f'N = {N}')
yekun = []
for i in N:
    cavab = 0
    for j in range(0, i + 1):
        suret = (cos((j ** 2) + 1) ** j) ** j
        mexrec = log(8, 3) * ((j + j ** 2) ** j)
        cavab += suret / mexrec
    yekun += [round(cavab, 2)]
print(f' List = {yekun}')

#tapsiriqda verilen
from math import cos, log
N = [6, 2, 5, 3, 9, 7, 4]
print(f'N = {N}')
yekun = []
cavab = 0
for i in N:
    for j in range(0, i + 1):
        suret = (cos((j ** 2) + 1) ** j) ** j
        mexrec = log(8, 3) * ((j + j ** 2) ** j)
        cavab += suret / mexrec
    yekun += [round(cavab, 2)]
print(f' List = {yekun}')'''

#21 Massivi [-100, 100] intervalında təsadüfi ədədlərlə doldurun (ədədlərin sayı = 8). Elementlərin yerlərini elə dəyişdirin ki, bütün müsbət elementlər massivin əvvəlində, 0 və bütün mənfi elementlər isə massivin sonunda yerləşdiren proqram
'''from random import randint
list1 = [randint(-100, 100) for i in range(8)]
print(f'A = {list1}')
menfi = []
musbet = []
for i in list1:
    if i > 0:
        musbet += [i]
    else:
        menfi += [i]
print(f' B = {musbet + menfi}')'''

#22 Massivi [0, 100] aralığında təsadüfi ədədlərlə doldurun (ədədləriin sayı = 10) və həmin massivdən Fibonaççi ardıcıllığına aid olan ədədləri seçib digər massivə köçüren proqram
'''def fibo():
    a = 0
    b = 1
    c = a + b
    fibo = [1]
    for i in range(9):
        a = b
        b = c
        c = a + b
        fibo += [c]
    return fibo
fibonacci = fibo()
from random import randint
list1 = [randint(0, 100) for i in range(10)]
print(f'List1 = {list1}')
yekun = []
for i in list1:
    if i in fibonacci:
        yekun += [i]
print(f' List2 = {yekun}')'''

#23 Listdəki 2-ci minimum və 2-ci maksimum ədədi tapan proqram
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = [randint(0, 100) for i in range(n)]
print(f'List = {a}')
yeni = []
maxx = float('-inf')
minn = float('inf')
for i in range(len(a)):
    if a[i] > maxx:
        maxx = a[i]
        yermax = i
    if a[i] < minn:
        minn = a[i]
        yermin = i
for k in range(len(a)):
    if k != yermax and k != yermin:
        yeni += [a[k]]
maxx2 = float('-inf')
minn2 = float('inf')
for i in range(len(yeni)):
    if yeni[i] > maxx2:
        maxx2 = yeni[i]
    if yeni[i] < minn2:
        minn2 = yeni[i]
print(f'Maksimal={maxx}, {maxx2}')
print(f'Minimal={minn}, {minn2}')'''

#24 Massivi təsadüfi ədədlər ilə doldurun və iki maksimal elementi və onların sıra nömrələrini tapan proqram
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = [randint(1, 5) for i in range(n)]
print('Massiv:')
print(*a)
yeni = []
maxx = float('-inf')
for i in range(len(a)):
    if a[i] > maxx:
        maxx = a[i]
        yermax = i
for k in range(len(a)):
    if k != yermax:
        yeni += [a[k]]
maxx2 = float('-inf')
for i in range(len(yeni)):
    if yeni[i] > maxx2:
        maxx2 = yeni[i]
for i in range(len(a)):
    if a[i] == maxx2 and i != yermax:
        yermax2 = i
print(f'Maksimal element: A[{yermax}]={maxx}')
print(f'Ikinci maksimum: A[{yermax2}]={maxx2}')'''

#25  Klaviaturadan massivi daxil edin və bir gedişdən istifadə etməklə maksimal qiymətə malik olan elementlərin sayını tapan proqram
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = [randint(1, 5) for i in range(n)]
print('Massiv:')
print(*a)
count = 0
maxx = float('-inf')
for i in range(len(a)):
    if maxx <= a[i]:
        maxx = a[i]
for i in a:
    if i == maxx:
        count += 1
print(f' Maksimal qiymet {maxx}')
print(f' Elementlerin sayi {count}')'''

#26 Massivdə cüt sayda element var. Massivi təsadüfi elementlərlə doldurun. Massivin 1-ci və 2-ci yarısı üçün ayrı-ayrılıqda inversiya əməliyyatını yerinə yetiren proqram
'''from random import randint
n = int(input('Uzunlugu daxil edin: '))
a = [randint(1, 5) for i in range(n)]
if n % 2 == 0:
    print('Massiv: E')
    print(f' {a}')
    firsthalf = a[(len(a) // 2) - 1::-1]
    secondhalf = a[-1:len(a) // 2 - 1:-1]
    yekun = firsthalf + secondhalf
    print('Half-Inverted')
    print(f' {yekun}')
else:
    print('Xeta, cut eded daxil edin.')

#o biri pdfde
def ekob(a, b):
    if a > b:
        minn = b
    else:
        if a < b:
            minn = a
        else:
            print('a = b')
    while True:
        if a % minn == 0 and b % minn == 0:
            ebob = minn
            break
        else:
            minn -= 1
    return (a * b) // ebob
from random import randint
n = int(input('Input: N='))
a = [randint(100, 200) for i in range(n)]
kublarcemi = []
yekun = []
if n % 2 == 0:
    print(f'List1 = {a}')
    for i in a:
        cem = ((i % 10) ** 3) + ((i // 10 % 10) ** 3) + ((i // 100) ** 3)
        kublarcemi += [cem]
        cem = 0
    for i in range(0, len(kublarcemi), 2):
        yekun += [ekob(kublarcemi[i], kublarcemi[i + 1])]
    print(f' List1_EKOB = {yekun}')
else:
    print('Xeta, N cut eded olmalidir.')'''

#27 Təsadüfi cümlələrdən hekayə düzəldən proqram
'''from random import randint
article_list = ["the", "a", "one", "some", "any"] 
noun_list = ["boy", "girl", "dog", "town" , "car"] 
verb_list = ["drove", "jumped", "ran", "walked" , "skipped"]  
preposition_list = ["to", "from", "over", "under" , "on"]
F_article_list = ["The", "A", "One", "Some", "Any"]
cumle = []
for i in range(5):
    cumle += [F_article_list[randint(0,4)]] + [noun_list[randint(0,4)]] + [verb_list[randint(0,4)]] + [preposition_list[randint(0,4)]] + [article_list[randint(0,4)]] + [noun_list[randint(0,4)]]
    cumle += ['.']
print(*cumle)'''

#28 Hər bir qiymətin hansı hərfdən neçə ədəd olduğu müəyyənləşdiren proqram
'''def qiymettap(a):
    if 91 <= a <= 100:
        return 'A'
    elif 81 <= a < 91:
        return 'B'
    elif 71 <= a < 81:
        return 'C'
    elif 61 <= a < 71:
        return 'D'
    elif a < 61:
        return 'E'
print('0-100 arasinda qiymetlerinizi daxil edin: ')
fenler = ['fizika', 'riyaziyyat', 'kimya', 'ingilis dili', 'ana dili']
cavab = []
for i in fenler:
    qiymet = int(input(f'{i} imtahanin qiymeti: '))
    cavab += [qiymet]
print(f'cavablariniz:  {cavab}')
asay, bsay, csay, dsay, kesir = 0, 0, 0, 0, 0
for i in cavab:
    if qiymettap(i) == 'A':
        asay += 1
    elif qiymettap(i) == 'B':
        bsay += 1
    elif qiymettap(i) == 'C':
        csay += 1
    elif qiymettap(i) == 'D':
        dsay += 1
    elif qiymettap(i) == 'E':
        kesir += 1
print('sizin qiymetleriniz: ')
print(f' {asay} eded A,')
print(f' {bsay} eded B,')
print(f' {csay} eded C,')
print(f' {dsay} eded D, ve')
print(f' {kesir} eded kesriniz var')'''

#29 “Hə”lərin sayına görə proqram sizə vəziyyət ilə bağlı mesaj veren proqram
'''fenler = ['fizika', 'riyaziyyat', 'kimya', 'ingilis dili', 'ana dili']
cavablar = []
for i in fenler:
    cavab = input(f'{i} imtahanini kecdiniz mi? he/yox ')
    cavablar += [cavab]
print(f'cavablariniz:  {cavablar}')
print('Sizin tedris veziyyetiniz beledir:')
heler = 0
for i in cavablar:
    if i == 'he':
        heler += 1
if 4 <= heler <= 5:
    print('elaci')
elif heler == 3:
    print('yaxshi')
elif 2 <= heler < 3:
    print('kafi')
else:
    print('pis')'''
