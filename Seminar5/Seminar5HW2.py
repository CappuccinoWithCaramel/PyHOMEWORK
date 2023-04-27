def sum(a,b):
    if b == 0:
        return a+b
    else:
        return sum(a+1,b-1)
    
a = int(input('Введите число А: '))
b = int(input('Введите число B: '))

print(sum(a,b))