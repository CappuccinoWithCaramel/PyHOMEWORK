n = int(input('Введите количество э-ов первого множества: '))
m = int(input('Введите количество э-ов второго множества: '))

list_n = set()
list_m = set()

for c in range(n):
    list_n.add(int(input()))

for i in range(m):
    list_m.add(int(input()))

print(list_n)
print(list_m)

print(sorted(list_n.intersection(list_m)))