n = int(input('Введите количество монеток на столе '))

import random

coin_counter = 0
reshka_counter = 0

while coin_counter <= n:
    curent_coin = bool(random.choice([True,False]))
    coin_counter += 1
    print(curent_coin)
    if curent_coin == True:
        reshka_counter += 1

print(f'Нам необходимо перевернуть {reshka_counter} монеток что-бы все монетки были перевернуты одной стороной')