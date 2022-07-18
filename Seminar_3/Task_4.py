# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def digit_check():
    try:
        lenght = int(input('Введите число:\n'))
        return lenght
    except ValueError:
        print('Это должно быть число!\n')
        digit_check()


num = digit_check()


def get_binary(number):
    number_binary = ' '
    while number > 0:
        number_binary += str(number % 2)
        number //= 2
        rev_num_bin = ''.join(reversed(number_binary))
    return rev_num_bin


num_bin = get_binary(num)
print(num_bin)
