def verse(characteristic, objects) -> int:
    return sum(map(characteristic, objects))



new_list = 'Ехал грека через реку, видит грека-в реке рак, сунул грека руку в реку, рак-греку за руку цап'

if verse(lambda x: x in 'ёйуеаоэяию', new_list) % 2 == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')