dig = int(input())
firstsum = 0
secondsum = 0
while dig > 999:
    fdig = dig % 10
    firstsum = firstsum + fdig
    dig = dig // 10
while dig > 0:
    sdig = dig % 10
    secondsum = secondsum + sdig
    dig = dig // 10
if firstsum == secondsum:
    print ('Ticket is HAPPY, HOORAY')
else:
    print ('Ticket is normal :(')