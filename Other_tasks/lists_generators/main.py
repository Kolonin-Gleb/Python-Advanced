# n = 5
# a = [0] * n
# print(a)


# Генераторы списков
'''
Для создания списков заполненных по
сложным формулам исп. генераторы.

Общий вид генератора:
[действия for переменной in последовательность]
'''

# zeros = [0 for i in range(5)]
# print(zeros)

# squares_of_digits = [i ** 2 for i in range(5)]
# print(squares_of_digits)

# Правая граница range - не включается
# squares_of_digits = [i ** 2 for i in range(1, 5)]
# print(squares_of_digits)


# Заполнение списка с помощью генератора
# a = [int(s) for s in input().split()]
# print(a)


