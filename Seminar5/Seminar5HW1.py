def stepka(a,b):
    if b ==0:
        return 1
    else:
        return a * stepka(a,b-1)


a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(stepka(a,b))