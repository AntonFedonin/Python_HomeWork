# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from os import system
from time import time


def random_num(minimum, maximum):
    now = str(time())
    rnd = float(now[::-1][:3])/1000
    return minimum+rnd*(maximum-minimum)


system("cls")
print('Хотите случайных чисел? Их есть у нас!')
print('Укажите диапозон чисел от минимума до максимума')
min = int(input('От: '))
max = int(input('До: '))
random = random_num(min, max)
print('Вот Вам случайное число: ', random)

