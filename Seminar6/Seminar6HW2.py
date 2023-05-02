import random

list_1 = [random.randint(-10, 10) for _ in range (10)]
print(list_1)

min_num = int(input())
max_num = int(input())

print([i for i in range(len(list_1)) if min_num <= list_1[i] <= max_num])