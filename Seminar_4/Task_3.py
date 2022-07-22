# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]


n = int(input('Введите число: '))
div = 2
res_lst = []

while n > 1:
    while n % div == 0:
        res_lst.append(div)
        n = n/div
    # div += 1
    if div == 2:
        div += 1
    else:
        div += 2
print(res_lst)
