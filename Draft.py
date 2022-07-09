run = True
while run:
    a = input('Введите число: ')
    print(a)
    print(a.isdigit())
    print(type(a))
    a1 = int(a)
    print(type(a1))
    run = True if input('Ещё раз? y/n ') == 'Y' or 'y' else False
    break
