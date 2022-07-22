# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить,
# используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

# Пример:

# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1
from cmath import pi
import math


def pi_num_Leybnic():
    n = 1
    const = 4
    pi_num = 0
    count = 1
    for i in range(50000):
        if count % 2 != 0:
            pi_num += (const/n)

        else:
            pi_num -= (const/n)
        count += 1
        n += 2
    return pi_num


my_pi = pi_num_Leybnic()
check = pi
print(my_pi)
print(check)
