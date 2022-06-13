# Функции map можно передать несколько последовательностей.
# В этом случае функция-обработчик будет получать элементы сразу из нескольких последовательностей
'''
def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
numbers3 = [100, 200, 300, 400, 500]

new_numbers = list(map(func, numbers1, numbers2, numbers3))
print(new_numbers)
'''

# Округление значений списка, с помощью map
'''
circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]

result1 = list(map(round, circle_areas, [1]*len(circle_areas))) # округляем числа до 1 знака после запятой
# [1]*len(circle_areas) - создаст список длины circle_areas полный 1, что позволит округлить все эл. до 1

print("Original: ", circle_areas)
print("Rounded: ", result1)
'''

# Встроенную функцию reduce, необходимо импортировать

from functools import reduce
import operator # Чтобы не реализовывать стандартные операции
# К примеру для конкатенации списка слов через reduce без него придётся делать свою реализацию +

words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs'] 
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

concat_words = reduce(operator.add, words)
print(type(concat_words), concat_words)
opposite_numbers = list(map(operator.neg, numbers))
print(opposite_numbers)
