# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.


import re

input_string = input('Напишите редактируемый текст: ')


def add_in_file(string):
    file = open('Text.txt', 'w')
    file.writelines(string)
    file.close()
    return(file)


def read_and_get_from_file(file):
    with open('Text.txt', 'r') as file:
        for line in file:
            string = line
    return string


def edit_file(string):
    string = re.sub("[^А-Яа-я- ]", "", string)
    return string


def write_in_file(string):
    with open('Text.txt', 'a') as file:
        file.write('\n' + string)


new_file = add_in_file(input_string)
output_string = read_and_get_from_file(new_file)
output_string = edit_file(output_string)
new_file = write_in_file(output_string)
print('Всё готово! Проверьте файл.')
