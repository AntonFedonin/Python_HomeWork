# 5- Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from os import system
import math

def find_dist():
    system('cls')
    print('Введите координаты точки A')
    x1 = float(input('X1 = '))
    y1 = float(input('Y1 = '))
    print('Введите координаты точки B')
    x2 = float(input('X2 = '))
    y2 = float(input('Y2 = '))
    result = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print('A (', x1, ',', x2, ') ; B (', y1, ',', y2, ') ->', round(result, 2))
find_dist()
while True:
    key = input('Попробуем ещё разок? [y/n]: ')

    if key == 'y':
        find_dist()
    else:
        break
