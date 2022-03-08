# Плохой пример создания вложенного списка
"""
n, m = int(input()), int(input())

my_list = [[0] * m] * n
my_list[0][0] = 17 # При изменении значения по индексу в 1 списке,
# это значение будет изменено во всех других списках тоже

# Это происходит т.к.:
# В Python списки – ссылочный тип данных.
# Конструкция [0] * m возвращает ccылку на список из m нулей.
# Повторение этого элемента создает список из n ссылок на один и тот же список.

# my_list - список из n ссылок на один и тот же список
print(my_list)
"""

# Создание 2х мерного списка с клавиатуры
'''
count_of_inner_lists = int(input("Введите кол. вложенных списков: "))

lst_2d = []
lst_1d = []

for ls in range(count_of_inner_lists):
    print("Введите через пробел эл. вложенного списка № " + str(ls))
    inner_list = [int(el) for el in input().split()]
    lst_2d.append(inner_list)
    lst_1d.extend(inner_list)

print("Ваш 2х мерный список")
print(lst_2d)
print("Ваш список в виде 1 мерного списка.\n Каждый вложенный список присоединслся к концу")
print(lst_1d)
'''

# step 7
'''
my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0] # [12, 221, 3]
minimum = my_list[0][0] # [12, 221, 3]

# Важно понять, как происходит сравнения числа и списка чисел

for row in my_list:
    if max(row) > maximum: # Происходит сравнения числа и первого эл. в списке
        print( str(max(row)) + " > " + str(maximum) )
        maximum = max(row) # 221 633 633
        
    if min(row) < minimum:
        print( str(min(row)) + " < " + str(minimum) )
        minimum = min(row) # 3 3 3

print(maximum + minimum) # 633 + 3 = 636
'''

# step 8
'''
n = int(input())
lst = [] # Список для вложенных списков

for i in range(n):
    # Формирование вложенного списка
    inner_lst = [i + 1 for i in range(n)]
    # Добавление вложенного списка
    lst.append(inner_lst)

print(*lst, sep='\n') # Каждый вложенный список выводим с новой строки
'''

# step 9
'''
n = int(input())
lst = [] # Список для вложенных списков
length_of_lst = 1

for i in range(n):
    # Формирование вложенного списка
    inner_lst = [i + 1 for i in range(length_of_lst)]
    # Добавление вложенного списка
    lst.append(inner_lst)
    # Изменение размера для следующего вложенного списка
    length_of_lst += 1

print(*lst, sep='\n') # Каждый вложенный список выводим с новой строки
'''
