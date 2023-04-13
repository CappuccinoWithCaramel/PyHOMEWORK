sum = 0
dig =int (input())
while dig > 0 :
    ost = dig % 10
    sum = sum + ost
    dig = dig // 10
print (sum)