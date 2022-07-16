# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


num = input("Введите целое число или дробное через точку: ")


def get_mult_fractional(a, b):
    mult = 1
    while (a != 0):
        mult = mult * (a % 10)
        a = a // 10
    while (b != 0):
        mult = mult * (b % 10)
        b = b // 10
    return mult


def get_mult_integer(a):
    mult = 1
    while (a != 0):
        mult = mult * (a % 10)
        a = a // 10
    return mult


if num.isdigit():
    prod = get_mult_integer(int(num))
else:
    find_num = num.split(".")
    integer = int(find_num[0])
    fractional = int(find_num[1])
    prod = get_mult_fractional(integer, fractional)


print("Произведение цифр равно:", prod)
