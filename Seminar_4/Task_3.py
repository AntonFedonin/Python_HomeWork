# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

def digit_check():
    try:
        lenght = int(input('Введите число:\n'))
        return lenght
    except ValueError:
        print('Должно быть число!:\n')
        digit_check()


def get_multipliers(number):
    div = 2
    result_lst = []
    while number > 1:
        while number % div == 0:
            result_lst.append(div)
            number = number/div
        # div += 1
        if div == 2:
            div += 1
        else:
            div += 2
    return result_lst


n = digit_check()
res_lst = get_multipliers(n)
print(res_lst)
