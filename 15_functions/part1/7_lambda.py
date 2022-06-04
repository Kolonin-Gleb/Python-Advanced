# Анонимные функции

# Анонимные функции – функции с телом, но без имени.

'''

def standard_function(x): #  стандартное объявление функции
    return x*2

lambda_function = lambda x: x*2 #  объявление анонимной функции

print(standard_function(7))
print(lambda_function(7))
'''
# Анонимные функции очень часто используются вместе со встроенными функциями map(),
# filter(), reduce(), sorted(), max(), min() и т.д.
'''
from functools import reduce 

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: True if name == name[::-1] and len(name) > 4 else False, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)
'''

# Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce()
# выводит в алфавитном порядке список primary городов с населением более 10.000.000 человек, в формате:
# Cities: Beijing, Buenos Aires, ...

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

# Выборка городов по условию
cities = list(filter(lambda city: True if city[2] == 'primary' and city[1] > 10000000 else False, data))
# Оставляю только названия городов
cities = list(map(lambda city: city[0], cities))
# Сортировка в алфавитном порядке
cities = sorted(cities)
print("Cities: ", end='')
print(*cities, sep=', ')