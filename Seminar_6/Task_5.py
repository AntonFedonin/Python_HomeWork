# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, \
#     второй и предпоследний и т.д.
import math

numbers = [4, 7, 1, 8, 2, 6, 0, 4, 2, 5, 7, 4, 9, 4, 3]


def mult_list(nums):
    return [nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]

print(mult_list(numbers))