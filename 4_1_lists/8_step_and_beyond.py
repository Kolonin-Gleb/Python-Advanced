# # Python: коллекции (индексирование, срезы, сортировка)
# # Статья https://habr.com/ru/post/319200/


# # С помощью срезов можно менять значения эл.,
# # удалять и добавлять новые эл.

# # Задача со stepik

# numbers = [4, 8, 12, 16, 34, 56, 100]
# numbers[1:4] = [20, 24, 28]
# # print(numbers) # 4, 20, 24, 28, 34, 56, 100

# # Lst[ Start(included) : End(not included) : Step ]
# # By default: Lst[ 0 : length of list(last el included) : 1]

# numbers = [5, 10, 15, 25]
# print(numbers[::-2]) #
# print(numbers[0:4:-2]) #

# # Почему результирующий срез - разный?


numbers = [5, 10, 15, 25]
# print(numbers[::-2])

# Создание копии списка

letters = ['a', 'b', 'c', 'd']

copied_letters = letters.copy()
# print(copied_letters)


# Соединение эл. списка в строку

words = ['Hello', 'Python']
# print('-'.join(words))


# numbers = [10, 20, 30, 40]
# del numbers[0:1]

# print(numbers)

