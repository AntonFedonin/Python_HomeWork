# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер,
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

# , 'basic', 'fortran', 'java', 'c++',
program_language = ['python', 'c#', 'pascal']
# 'delphi', 'php', 'javascript', 'kotlin', 'sql', 'assembler', 'Plankalkül']
num_list = [i for i in range(1, len(program_language)+1)]

# print(program_language)
print(num_list)
program_language = [program_language[i].upper()
                    for i in range(len(program_language))]
# program_language = map(lambda i: program_language[i].upper(), program_language)  В случае приминения функции "map", функция "upper()" не работает(
print(program_language)


def get_tuple(language, numbers):
    find_tuple = [(numbers[i], language[i]) for i in range(len(numbers))]
    return find_tuple


def get_point(prog):
    point_list = []
    for i in range(len(prog)):
        summa = 0
        for j in range(len(prog[i])):
            summa += ord(prog[i][j])
        point_list.append(summa)
    return point_list

# find_list=filter(lambda x: )
point = get_point(program_language)
print(point)
ftuple = get_tuple(program_language, num_list)
print(ftuple)
