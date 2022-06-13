# Функции высшего порядка - те, что принимают или возвращают функции

# Они часто используются для обработки наборов данных

# Функция map() - одинаковое преобразование эл. списка
'''
# function - функция, преобразования элементов
def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result

def square(x):
    return x**2


def cube(x):
    return x**3

numbers = [1, 2, -3, 4, -5, 6, -9, 0]

strings = map(str, numbers)        # используем в качестве преобразователя - функцию str
abs_numbers = map(abs, numbers)    # используем в качестве преобразователя - функцию abs

squares = map(square, numbers)     # используем в качестве преобразователя - функцию square
cubes = map(cube, numbers)         # используем в качестве преобразователя - функцию cube

print(strings)
print(abs_numbers)
print(squares)
print(cubes)
'''

# Функция filter() - отобрать часть элементов списка по определенному критерию
'''
def filter(function, items):
    result = []
    for item in items:
        if function(item):        
            result.append(item)
    return result

def is_greater10(num): # функция возвращает значение True если число больше 10 и False в противном случае
    return num > 10


numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
large_numbers = filter(is_greater10, numbers) # список large_numbers содержит элементы, большие 10
print(large_numbers)
'''

# Функция reduce() - формированием результирующего значения при комбинации элементов с использованием аргумента-аккумулятора.
'''
def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc

def add(x, y):
    return x+y

def mult(x, y):
    return x*y

numbers = [1, 2, 3, 4, 5]

total = reduce(add, numbers, 0)
product = reduce(mult, numbers, 1)

print(total)
print(product)
'''

'''
numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

var1 = max(numbers, key=abs)
var2 = min(map(abs, numbers))

print(var1 + var2)
'''

'''
def map(function, items):
    result = []
    for item in items:
        result.append(cube(item))
    return result

def cube(digit):
    return digit**3

def filter(function, items):
    result = []
    for item in items:
        if checker(item):
            result.append(item)
    return result

def checker(digit):
    if digit >= 100 and digit <= 999:
        if digit % 5 == 2:
            return True
    return False

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

# отбирает из заданного списка numbers трёхзначные числа,
# дающие при делении на 55 остаток 22, 

chosen_nums = filter(checker, numbers)

resulting_nums = map(cube, chosen_nums)
# и выводит их кубы, каждый в отдельной строке.

for i in resulting_nums:
    print(i)
'''

# tasks
'''
Вывод суммы квадратов двузначных чисел, которые делятся на 7 без остатка.
'''

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def is_devided_by_7(item):
    if item % 7 == 0: return True
    else: False

def square(item):
    return item ** 2

numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

chosen_nums = [num for num in numbers if len(str(num).replace('-','')) == 2] # 2х значные числа
print(chosen_nums)
chosen_nums = filter(is_devided_by_7, chosen_nums)
print(chosen_nums) # кратные 7
squares = map(square, chosen_nums)
print(sum(squares))
