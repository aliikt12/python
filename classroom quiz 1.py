#Tapsiriq 1 Dalgali ededlerin axtarisi
'''start = int(input('Starti daxil edin: '))
end = int(input('Endi daxil edin: '))
dalga_siyahisi = []
def reqem(a):
  if a >= 100:
    reqemler = []
    copy = a
    while a:
      reqemler += [a % 10]
      a //= 10
    for i in range(len(reqemler) - 2):
      if ((reqemler[i] < reqemler[i + 1]) and (reqemler[i + 1] > reqemler[i + 2])) or ((reqemler[i] > reqemler[i + 1]) and (reqemler[i + 1] < reqemler[i + 2])):
        return True
      else:
        return False
  else:
    print('Eded 100-den kicikdir.')
for j in range(start, end + 1):
  if reqem(j):
    dalga_siyahisi += [j]
print(f'{start}-{end} araligindaki dalga ededler: {dalga_siyahisi}')'''

#Tapsiriq 2 Mexfi temperatur melumatlarinin berpasi
'''def maxi(a):
  maxx = float('-inf')
  for i in a:
    if maxx < abs(i):
      maxx = abs(i)
  return maxx
n = int(input('Listin uzunlugunu daxil edin: '))
a = [int(input()) for i in range(n)]
yekun = []
maxa = maxi(a)
print(f'Input (Sifrelenmis siyahi): {a}')
for i in a:
  yekun += [i + maxa]
print(f'Output (Orijinal siyahi): {yekun}')'''

#Tapsiriq 3 Daxil edilen noqtenin oblasta aid olmasinin yoxlanisi
'''from math import sin
x = float(input('X-i daxil edin: '))
y = float(input('Y-i daxil edin: '))
if ((x * 2) + (y * 2) <= 30) and ((y <= (2 * x) - 3 and y >= sin(x)) or (y <= sin(x) and y >= (2 * x) - 3 and x >= -5 and y >= -3)):
  print(f'Verilen ({x},{y}) noqtesi oblasta daxildir.')
else:
  print(f'Verilen ({x},{y}) noqtesi oblasta daxil deyildir.')'''

#Tapsiriq 4 Ters-Harshad eded
'''def harshad(a):
  cem = 0
  copy = a
  while a:
    digit = a % 10
    cem += digit
    a //= 10
  qismet = copy // cem
  if copy % cem == 0 and qismet > cem:
    return True
  return False
a = int(input('Starti daxil edin: '))
b = int(input('Endi daxil edin: '))
print(f'Interval: {a}-{b}')
print(f'({a},{b} intervalindaki ters harshad ededler: ')
for i in range(a, b + 1):
  if harshad(i):
    print(i, end = ' ')'''

