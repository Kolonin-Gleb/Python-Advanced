# Создание множества

# languages = {'Python', 'Cpp', 'JS', 1001}

# Множество - неупорядоченный набор данных. Порядок эл. в нём может меняться
# print(languages)

# Пустое множество через встроенную функцию

# Создание пустого множества
# members = set()
# print(type(members))
# # Создание словаря
# clan = {} # Создаётся пустой словарь, а не множество
# print(type(clan))
'''
myset1 = set(range(10)) # множество из элементов последовательности
print(myset1)
# Множество из символов строки
myset2 = set('1234')
print(myset2)

# Множество слов
myset3 = {'asdf', 'asdfasdf', 'asdfasdcvzxcv'}
print(myset3)
myset3 = set(['asdfdafsdfxzcvz', 'asdfasdf', 'asdfasdcvzxcv'])
print(myset3)
'''

# Элементами множества могут являтся только 
# неизменяемые объекты. Cписок не может быть эл. множества
# mysetik = {1, 2, [3, 4, 5]}

# множество не может содержать множество
# setik = {9, 0, {3, 4, 5}}

# Множество - изменяемая коллекция с неизменяемыми элементами

my_set = {}
print(type(my_set))
print(my_set)

my_set = set([''])
print(type(my_set))
print(my_set) # Множество, содержащие список из 2х эл

my_set = set('')
print(type(my_set))
print(my_set)

my_set = set(())
print(type(my_set))
print(my_set)

my_set = set()
print(type(my_set))
print(my_set)

my_set = set([])
print(type(my_set))
print(my_set)

myset = set([1, 2, 3, '1', '2', '3']) # [] нужны, т.к. set() - может принять только 1 аргумент, который может быть перечисляемым
print(len(myset))
print(myset)


