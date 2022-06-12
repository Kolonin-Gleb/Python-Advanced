# Методы словарей

# Подсчёт кол. эл. в списке с помощью словаря
'''
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    if num not in result:
        result[num] = 1 # Создание новой пары ключ-значение
    else:
        result[num] += 1 # Изменение значения по ключу

print(result)
'''

# Чтобы избежать возникновения ошибки в случае отсутствия ключа в словаре можно использовать метод get(),
'''
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

# get(ключ, значение если ключ не обнаружен)

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
'''

# Метод update() - добавляет в словарь пары ключ-значение из 2 словаря. При совпадении ключей останется значение из передаваемого словаря.
'''
info1 = {
    'name': 'Bob',
    'age': 25,
    'job': 'DS'
}

info2 = {
    'age': 30,
    'city': 'New York',
    'email': 'bob@web.com'
}

info1 |= info2
print(info1)
'''
# setdefault - получает знач из словаря по ключу или добавляет пару ключ - знач


# tasks
'''
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict1

# Добавляем новые пары и увеличиваем значения для пар, что уже существуют
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value
print(result)
'''

# Посчитать кол. вхождений каждого символа в строку
'''
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}

for sym in text:
    result[sym] = result.get(sym, 0) + 1

print(result)
'''

# Самое частое слово (слова в алфавитном порядке)
'''
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

result = {}

for word in s.split():
    result[word] = result.get(word, 0) + 1

# Определение максимального значения среди ключей
maximum = max(result.values())

most_mentioned_words = []

# Взятие ключей с максимальным значением
for key, value in result.items():
    if value == maximum:
        most_mentioned_words.append(key)

# Вывод наименьшего слова по алфавиту
print(sorted(most_mentioned_words)[0])
'''

# pets
'''
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

# Отдельно сформирую все ключи и их значения. Потом объединю
keys = []
values = []
for pet in pets:
    if pet[1::] in keys: # Если такой ключ уже существует, значит у этого человека > 1 животного
        values[keys.index(pet[1::])].append(pet[0])
    else:
        keys.append(pet[1::])
        values.append([pet[0]])

for index, key in enumerate(keys, 0):
    result[key] = values[index]

print(result)
# Более элегантное решение

result = {}
for pet in pets:
    result.setdefault(pet[1:], []).append(pet[0])

# print(result)
'''

# Самое редкое слово
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке, т.е. идёт раньше ПО АЛФАВИТУ
'''
s = input().lower()
# Удаление пунктуации
for sym in s:
    if sym in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
        s = s.replace(sym, '')

result = {}

for word in s.split():
    result[word] = result.get(word, 0) + 1

# Определение минимального значения среди ключей
minimum = min(result.values())

rarest_words = []
# Взятие ключей с максимальным значением
for key, value in result.items():
    if value == minimum:
        rarest_words.append(key)

# Вывод наименьшего слова по алфавиту среди самых редких
print(sorted(rarest_words)[0])
'''

# Удаление дубликатов
'''
data = input().split()
frequency = {}

for i in data:
    frequency[i] = frequency.get(i, 0) + 1

# print(frequency)
answer = []
for elem in data[::-1]: # Иду по элментам списка data с конца.
    if frequency[elem] > 1: # Тем элементам, что встречаются > 1 раза
        # добавляю _число-из-frequency
        answer.append(f"{elem}_{frequency[elem]-1}")
        frequency[elem] -= 1 # Уменьшаю кол. этого эл. в frequency
    else:
        answer.append(elem)

print(*answer[::-1], end=" ")
'''
# Более элегантное решение
n = input().split()
d = {}
for i in n:
    d[i] = d.get(i, -1) + 1
    print(i if d[i] == 0 else f"{i}_{d[i]}", end=" ")
