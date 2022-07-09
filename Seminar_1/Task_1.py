# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
from os import system

def find_day():
  system("cls")
  day = input('Введите цифру, обозначающую день недели: ')
  if day.isdigit() == True:
    day = int(day)
    if day < 1 or day > 7:
       print('Ошибка! Необходимо число от 1 до 7')
    elif day < 6:
       print(day,'-> Нет')
    else:
       print(day,'-> Да')
  else:
    print('Ошибка! Необходимо ввести число')
find_day()
while True:
    key = input('Попробуем ещё разок? [y/n]: ')

    if key == 'y':
        find_day()
    else:
        break
