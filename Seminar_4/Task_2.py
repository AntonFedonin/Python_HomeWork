
# 2- Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# Посмотрели, что такое множество? Вот здесь его не используйте.

import random


num = [random.randint(0, 25)for i in range(0, 101)]


def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


uni_num = get_unique_numbers(num)
new_num = list(set(num))

print(num)
print(uni_num)
print(new_num)
