# Методы множеств часть 3
'''
set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}

print(set1.issubset(set2)) # Т.к. множество 1 явл. подмножеством множества 2 - вернёт True

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4, 5, 6}

# Нестрогое подмножество
print(set1 <= set2)

# Строгое подмножество
print(set1 < set2)

# Метод isdisjoint() - для проверки отсутствия общих эл. в множествах

set1 = {'b', 'e', 'g', 'k'}
set2 = {'b', 'e', 'g', 'k', 's', 't', 'p', 'i', 'k'}

print(set1 < set2) # True
'''

set1 = set(range(1, 10))
set2 = set(range(10, 20))

print(set1)
print(set2)

print(set1.isdisjoint(set2)) # Пересечение пустое - True

