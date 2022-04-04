'''
Словарь - изменяемая коллекция элементов с произвольными индексами - ключами
Для словаря индексы задаются любыми ключами, в том числе в виде строк

Словарь - реализация структуры данных "ассоциативный массив" или "хеш таблица".
В других языках эта структура данных называется map, HashMap, Dictionary
'''

# Создание словаря
languages = {
    'Pythonn': 'Gvido Van Rossum',
    'C++': 'Bjorne Stroustrupe',
    'Java': 'James Gosling',
    1: 'one'
}
# key : value

# print('Создателем языка C++ является', languages['C++'])
# print('Создателем языка C++ является', languages[1])

# Создание словаря встроенной функ. dict()
# key1 = value1, key2 = value2
info = dict(name = 'Timur', age = 28, job = "teacher")

# print(info)

# Создание словаря из списка кортежей
info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
info_dict = dict(info_list)
# print(info_dict)

info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков

info_dict = dict(info_tuple)  # создаем словарь на основе кортежа списков
# print(info_dict)



# Создание словаря, где у всех ключей одно и то же значение

dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missing info')
print(dict1)

# Начиная с версии Python 3.6 словари являются упорядоченными, то есть сохраняют порядок следования ключей
# в порядке их внесения в словарь.



# Создание словаря с использованием функции упаковщика zip()

keys = ['name', 'age', 'job']
values = ['Gleb', 17, None]

Gleb_info = dict(zip(keys, values))

print(Gleb_info)

