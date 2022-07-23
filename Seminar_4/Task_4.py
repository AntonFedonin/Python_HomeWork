# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.

import re

new_file = open('Text.txt', 'w')
input_str = input('Напишите редактируемый текст: ')
new_file.writelines(input_str)
new_file.close()
print(input_str)

with open('Text.txt', 'r') as new_file:
    for line in new_file:
        output_str = line
print(output_str)

output_str = re.sub("[0|1|2|3|4|5|6|7|8|9]", "", output_str)

with open('Text.txt', 'a') as new_file:
    new_file.write('\n' + output_str)
print(output_str)
