k = int(input())
n = int(input())
m = int(input())

if k > m*n:
    if k % n == 0 or k % m ==0:
        print ('No')
else:
    print ('Yep')