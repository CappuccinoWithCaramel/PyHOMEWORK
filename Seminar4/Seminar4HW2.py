n = int(input())
list = [int(input()) for i in range(n)]
counter = list()

for i in range(len(list)-1):
    counter.append(list[i-1]+ list[i]+ list[i+1])
counter.append(list[-2]+list[-1]+ list[0])
print(max(counter))