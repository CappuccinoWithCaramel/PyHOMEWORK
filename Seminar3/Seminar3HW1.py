n = int(input('Введите размер массива '))
x = int(input('Введите число X '))
counter_of_x = 0
array_of_numbers = [i+1 for i in range(n)]
for i in range(array_of_numbers[n-1]):
    if i == x:
        counter_of_x +=1

print(*array_of_numbers)
print(f'Число X встречается в массиве {counter_of_x} раз')

