# 3- Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

from os import system


system('cls')
x = float(input('Введите координату "X": '))
y = float(input('Введите координату "Y": '))

if x > 0 and y > 0:
    print('X =', x, '; Y =', y, '-> 1')
elif x < 0 and y > 0:
    print('X =', x, '; Y =', y, '-> 2')
elif x < 0 and y < 0:
    print('X =', x, '; Y =', y, '-> 3')
else:
    print('X =', x, '; Y =', y, '-> 4')
