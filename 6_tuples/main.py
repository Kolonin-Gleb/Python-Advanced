# Основы работы с кортежами ч. 2

# Операция распаковки кортежа. Также работает для списка
'''
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
languages = ['Python', 'C++', 'Java']

print(*numbers) # Распаковка. Получу содержимое без , и ()
print(*languages)

# Распаковка с специфическим выводом

print(*numbers, sep="\n")
'''

# Сравнение кортежей

# Сортировка кортежей


# Задача на кортеж

# Список из кортежей
'''
poets = [
    ('Есенин', 13),
    ('Тургенев', 14),
    ('Маяковский', 28),
    ('Лермонтов', 20),
    ('Фет', 15)
]
'''
# Это сортировка пузырьком (меньшие значения - более легкие - поднимаются вверх)
# По числам в кортежах
'''
for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i][1] > poets[j][1]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0]) # Самый младший (легкий)
print(poets[-1]) # Самый старший (тяжелый)
print(poets)
'''

# Это сортировка пузырьком
# По строкам в кортежах => алфавитный порядок => а - первый, я - последний
'''
for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i] > poets[j]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0])
print(poets[-1])
'''

# Произведение эл. кортежа
'''
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)

product = 1 # Произведение

for num in numbers:
    product *= num

print(product)
'''

# Распаковка кортежа
'''

colors = ('red', 'green', 'blue', 'cyan')

a, b, c, d = colors

# print(a)
# print(b)
# print(c)
# print(d)

colors = ('red', 'green', 'blue', 'black')
a, b, _, _ = colors

# print(a)
# print(b)

# a, b, c = 3, 2, 1
# print(a, b, c)
# b, a, c = c, a, b
# print(b, c, a)
'''


# tasks
'''
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2:1])
'''

# Вершина пароаболы
'''
a = int(input())
b = int(input())
c = int(input())

x = -b / (2*a)
y = (4*a*c-b**2) / (4*a)

print(tuple([x, y]))
'''

count = int(input())
tuples = []

for tup in range(count):
    name, score = tuple(input().split())
    tuples.append(tuple([name, int(score)]))

for tup in tuples:
    print(*tup)
print() # затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).
for tup in tuples:
    if tup[1] == 4 or tup[1] == 5:
        print(*tup)