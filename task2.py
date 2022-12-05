# 2.Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N   '))
list=[]
for i in range(2,n):
    while n%i==0:
        n=n//i
        list.append(i)
print(list)