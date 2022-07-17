# 3 - Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564

import math
import random


lst = []

for i in range(0, 10):
    lst.append(round(random.uniform(0, 10), 3))
print(lst)


def find_max(lst):
    max = lst[0] - math.floor(lst[0])
    for i in range(len(lst)):
        bfr = lst[i] - math.floor(lst[i])
        if bfr > max:
            max = bfr
    return max


def find_min(lst):
    min = lst[0] - math.floor(lst[0])
    for i in range(len(lst)):
        bfr = lst[i] - math.floor(lst[i])
        if bfr < min:
            min = bfr
    return min


def find_diff(min, max):
    difference = max-min
    return difference


min = find_min(lst)
max = find_max(lst)
diff = find_diff(min, max)
print(max)
print(min)
print(diff)
