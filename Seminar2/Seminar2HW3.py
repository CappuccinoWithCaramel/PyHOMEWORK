n = int(input('Введите число '))

curent_number = 1

while curent_number <= n:
    curent_number *= 2
    if curent_number >n:
        exit(0)
    print(curent_number, end=', ')