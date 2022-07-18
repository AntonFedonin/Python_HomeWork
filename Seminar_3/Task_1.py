# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def digit_check():
    try:
        lenght = int(input('Задайте размер списка:\n'))
        return lenght
    except ValueError:
        print('Это должно быть число!\n')
        digit_check()


# def get_list():  # Хотел сделать функцию заполнения списка. Почему-то она не хочет
#     list = []  # выполняться.
#     for item in range(0, 10):
#         list.append(random.randint(0, 10))
#     return list
size = digit_check()
lst = []
for i in range(0, size):
    lst.append(random.randint(0, 10))
print(lst)


def get_sum(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum


# lst = get_list()
summa = get_sum(lst)
# print(lst)
print('Сумма равна: ', summa)
