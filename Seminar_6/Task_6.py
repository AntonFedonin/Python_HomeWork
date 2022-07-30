# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

number = 5


def get_seq(num): return [-3 ** i for i in range(1, num+1)]


print(get_seq(number))
