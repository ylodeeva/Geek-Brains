Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#easy

#Дан список фруктов.
#Напишите программу, выводящую фрукты в виде нумерованного списка,выровненного по правой стороне.

a = ["яблоко", "банан", "киви", "арбуз"]
idx = 0
while idx < len(a):
  b = idx+1
  print ('{: >}'.format (b), a[idx])
  idx += 1
  
print ('-'*50)
  
#Даны два произвольные списка.
#Удалите из первого списка элементы, присутствующие во втором списке.

a = ["яблоко", "банан", "киви", "арбуз"]
b = ["киви", 23, 'flower']
a = set(a)
b = set(b)
c = a.difference (b)
print (str(c))

print ('-'*50)

#Дан произвольный список из целых чисел.
#Получите НОВЫЙ список из элементов исходного, выполнив следующие условия: если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n1= list()

for itm in n:
  if itm % 2 != 0:
    n1.append(itm*2)
  else:
    n1.append(itm/4)
print (n1)
print ('-'*50)


#normal

#Дан список, заполненный произвольными целыми числами, получите новый список, элементами которого будут квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и если такой корень вообще можно извлечь
#Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]

list1 = [2, -5, 8, 9, -25, 25, 4]
list2 = list()
for itm in list1:
  if itm >= 0:
    if (itm**0.5) == int(itm**0.5):
      list2.append(int(itm**0.5))
print (list2)
print ('-'*50)

#Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша Задание вывести дату в текстовом виде, например: второе ноября 2013 года/ Склонением пренебречь (2000 года, 2010 года)

from datetime import datetime

now_date = datetime.now()

month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня','июля','августа','сентября','октября','ноября','декабря']
month_idx = now_date.month - 1

result = "Сегодня {day} {month} {year} года".format(day=now_date.day, month=month_list[month_idx], year=now_date.year)
print(result)

print ('-'*50)

#Напишите алгоритм, заполняющий список произвольными целыми числами в диапазоне от -100 до 100. В списке должно быть n - элементов.
#Подсказка: для получения случайного числа используйте функцию randint() модуля random

import random

n = input("Введите количество элементов:")
n = int(n)

list_normal = list()
idx = 0
while idx <n:
  list_normal.append(random.randint(-100,100))
  idx +=1
print (list_normal)

print ('-'*50)

#Дан список, заполненный произвольными целыми числами.Получите новый список, элементами которого будут: 
#а) неповторяющиеся элементы исходного списка: например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#б) элементы исходного списка, которые не имеют повторений: например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
set_a = set(lst)
print (set_a)
set_b = list()
for itm in set_a:
  if lst.count(itm) == 1:
    set_b.append(itm)
print (set_b)

print ('-'*50)

#hard
#уравнение прямой вида y = kx + b задано в виде строки. Определить координату y точки с заданной координатой x. Вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
idx = 0
print (equation)
x = input('Введите х:')  
x = float(x)
d = equation.find('=')
f = equation.find('x')
k = float(equation[d+1:f])
#print ('k=', k)
g = equation.find('+')
b = float(equation[g+1:])
#print ('b=', b)
y = k*x+b
print ('y=', y)

print ('-'*50)

#Дата задана в виде строки формата 'dd.mm.yyyy'.
#Проверить, корректно ли введена дата.
#Условия корректности:
#1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#(в зависимости от месяца, февраль не учитываем)
#2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
#3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
#4. Длина исходной строки для частей должна быть в соответствии с форматом 
#(т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
#Пример корректной даты
#date = '01.11.1985'

date = input('Введите дату(dd.mm.yyyy):')
day = date[:2]
month = date[3:5]
year = date[6:]
#print (day, month, year)
if len(date) == 10:
  if 0 < int(day) < 32:
    if 0 < int(month) <13:
      if 0< int(year) <9999:
        print('Дата {} введена корректно'.format(date))
      else:
        print('Дата введена неверно')
    else:
      print('Дата введена неверно')
  else:
    print('Дата введена неверно')
else:
  print('Дата введена неверно')
print ('-'*50)

#"Перевёрнутая башня" (Задание олимпиадного уровня)


room = int(input('Введите номер комнаты:'))
block = 0
floor = 1
pos = 1 
onetage = 1

while (pos +(block * block)) <= room: 
    pos += (block * block)
    floor += block 
    block += 1 

while (pos + (onetage * block)) <= room :
    pos += onetage * block 
    onetage += 1 
floor += onetage - 1 

place = 1 
while (pos + place) <= room :
    place += 1
pos += place - 1

print('Floor:', floor)
print('Position:', place)
print ('-'*50)

  
