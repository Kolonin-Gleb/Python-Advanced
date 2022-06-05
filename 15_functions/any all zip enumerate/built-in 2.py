# Встроенные функции any(), all(), zip(), enumerate()


# all() и any() - для определения, выполняется ли некоторое условие одновременно
# для всех или хотя бы для одного эл последовательности


# Функции all() и any() в связке с функцией map()
'''
numbers = [17, 90, 78, 56, 231, 45, 54, 89, 91, 11, 19]

result = all(map(lambda x: x > 10, numbers))

if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')
'''

# Функция enumerate()
# Встроенная функция enumerate() возвращает кортеж из индекса элемента
# и самого элемента переданной ей последовательности
'''
colors = ['red', 'green', 'blue']

for pair in enumerate(colors, start=1):
    print(pair)
'''

# Функция zip()
# zip() объединяет отдельные элементы из каждой переданной ей последовательности в кортежи.
'''
numbers = [1, 2, 3]
words = ['one', 'two', 'three']

for pair in zip(numbers, words):
    print(pair)

# Example 2

numbers = [1, 2, 3, 4]
words = ['one', 'two']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result))
'''

# Частые сценарии использования функции zip()

# Создание словаря
'''
keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

info = dict(zip(keys, values))
print(info)
'''
'''
numbers = [10, 30, 20, 50, 40, 60, 70, 80]

total = 0
for index, number in enumerate(numbers, 1):
    if index % 2 == 0:
        total += number
print(total)

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

result = 0
for x, y in zip(list1, list2):
    result += x*y
print(result)
'''

# tasks
'''
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))

# Через all / any

print()

def ignore_command2(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(word in command for word in ignore)

print(ignore_command2('get ip'))
print(ignore_command2('select all'))
print(ignore_command2('delete'))
print(ignore_command2('trancate'))
'''

# zip step 9
# <capital> is the capital of <country>, population equal <population> people.

capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

pairs = zip(capitals, countries, population)

for capital, country, people in zip(capitals, countries, population):
    print(f'{capital} is the capital of {country}, population equal {people} people.')
