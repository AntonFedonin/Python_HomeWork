# 4-Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

from os import system


system('cls')
quarter = input('Введите номер четверти: ')
if quarter.isdigit()==True:
    quarter=int(quarter)
    if quarter<0 or quarter>4:
        print('Ошибка! Необходимо значение от 1 до 4')
    elif quarter==1:
        print('В первой четверти диапозон координат от X до Y')
    elif quarter==2:
        print('Во второй четверти диапозон координат от -X до Y')
    elif quarter==3:
        print('В третьей четверти диапозон координат от -X до -Y')
    elif quarter==4:
        print('В четвёртой четверти диапозон координат от X до -Y')
else:
    print('Ошибка! Неодходимо ввести число!')                    
            