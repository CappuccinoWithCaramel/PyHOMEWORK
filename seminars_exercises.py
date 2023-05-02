# def fibo(n):
#     if n in [0,1]:
#         return n
#     return fibo(n-1) + fibo(n-2)

# n = int(input())

# print(fibo(n))

# ------------------------------------------------------------------------------------------------------#


# import random

# marks = [random.randint(1,5) for _ in range (10)]
# print(marks)

# max_marks = max(marks)
# min_marks = min(marks)

# for i in range (len(marks)):
#     if marks[i] == max_marks: marks[i] = min_marks
# print(marks)

# --------------------------------------------------------------------------------------------------------#


# def prime_num(n , div):
#     if div == n// 2 +1:
#         print('Yes')
#     elif n % div == 0:
#         print (f'No, divider is {div}')
#     else:
#         prime_num(n,div+1)

# value = int(input('Enter number, please: '))
# prime_num(value,2)

# -----------------------------------------------------------------------------------------------------------#



# def print_seq(n : int, s=' ') -> str:
#     if n != 0 :
#         s = s + str(n) + ' '
#         return print_seq(n -1, s)
#     else:
#         return s + '0'


# n = int(input('Введите число: '))
# print(print_seq(n))


#--------------------------------------------------------------------------------------------------------------#



# import random

# list_1 = [random.randint(0, 10) for _ in range (10)]
# list_2 = [random.randint(0, 10) for _ in range (5)]

# result_list = [i for i in list_1 if i not in list_2]
# print(list_1)
# print(list_2)
# print(result_list)



#-----------------------------------------------------------------------------------------------------------------#





