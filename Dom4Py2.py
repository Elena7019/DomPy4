# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Задайте натуральное число: '))
lst = []
i = 2
number = n
while i <= n:
    if n % i == 0:
        lst.append(i)
        n //= i
        i = 2
    else:
        i += 1
print('Простыми множителями числа ', number, 'являются: ', lst)
