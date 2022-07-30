# 2- Найти сумму чисел списка стоящих на нечетной позиции


numbers = [12, 45, 3, 8, 234, 9, 5, 3, 10]


def get_sum(num):
    return sum(num[1::2])
                                    

print(get_sum(numbers))
