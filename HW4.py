# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

number = int(input("Введите число: "))
list_number = list()

# count = 1
# for i in range(1, number + 1):
#
#     count = count * i
#
#     list_number.append(count)

print(list(map((lambda x: math.factorial(x)), range(1, number + 1))))
