# Задача 1
# Вывести кортежи, что являются макс и мин по их ср. арифметическому
'''
from statistics import *

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

print(max(numbers, key=mean))
print(min(numbers, key=mean))
'''

# Задача 4
# Сортировать список кортежей по заданному полю.
# Не использовать условный оператор

# Принимает кортеж и возращает его 0 элемент
def compare_by_name(athlet):
    return athlet[0]

def compare_by_age(athlet):
    return athlet[1]

def compare_by_height(athlet):
    return athlet[2]

def compare_by_weight(athlet):
    return athlet[3]

def print_cortejes(lst):
    for i in lst:
        print(*i)

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

# словарь соответствия команда → функция сортировки
commands = {'1': compare_by_name, '2': compare_by_age, '3': compare_by_height, '4': compare_by_weight}

command = input() # считываем команды для выбора сортировки

# Сортируем в соответствии с выбранной опцией. Передаём в неё список для сортировки
athletes_to_print = sorted(athletes, key=commands[command])

print_cortejes(athletes_to_print)

