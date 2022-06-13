# Функции как объекты

# Любая функция в языке Python — объект типа function.
# print(type(print))
# print(type(sum))
# print(type(abs))

# Запись функции в переменную
# def hello():
#     print("hello")

# func = hello
# func()


# Функции в качестве аргументов других функций
# Функции высшего порядка - функции, способные принимать или/и возвращать другие функции.

# -- Может быть полезно при построении графиков разных функций.


# Встроенные функции, принимающие функции в качестве аргументов

# numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
# Стандартная реализация работы функций
# print(max(numbers))
# print(min(numbers))
# print(sorted(numbers))

# Их функционал можно изменить (В их реализации есть необязательный аргумент - key, передавая в который функцию можно изменить принцип работы)
# К примеру, я хочу, чтобы они работали по модулю

# print(max(numbers, key=abs))
# print(min(numbers, key=abs))
# print(sorted(numbers, key=abs))

# Функции в качестве возвращаемых значений других функций
'''
# Пример: функции квадратных трёхчленов

def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom

f = generator_square_polynom(a=1, b=2, c=1)
g = generator_square_polynom(a=2, b=0, c=-3)
h = generator_square_polynom(a=-3, b=-10, c=50)
# Теперь f g h хранят функцию generator_square_polynom с заданными параметрами

# Передаваемый в них параметр при вызове будет записан в x
print(f(1))
print(g(2))
print(h(-1))

# Замыкания – вложенные функции, ссылающиеся на переменные, объявленные вне определения этой функции,
# и не являющиеся её параметрами.
# Пример: функция square_polynom()
'''

'''
s1 = 'python'
s2 = 'stepicon'
s3 = 'beegeek'
 
print(min(s1, s2, s3))
print(max(s1, s2, s3))
'''

# Интересный подход к выполнению функции, соответствующей введённой команде
'''
def start():
    print('start')
def stop():
    print('stop')
def pause():
    print('pause')
def unknown():
    print('unknown command')

commands = {'start':start, 'stop':stop, 'pause':pause}
command = input()
commands.get(command, unknown)() # - Вернёт значение по ключу, т.е. функцию, которая будет выполняться Или вызовет команду, сообщающую о отсутствии команды
'''
# new tasks

# Сортировка по расстоянию от центра
'''
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
print(sorted(points, key=lambda cortej: (cortej[0]**2 + cortej[1]**2)**0.5))
'''

# Математические функции
'''
from math import sin, sqrt

def square(number):
    return number ** 2
def cube(number):
    return number ** 3

commands = {'квадрат': square, 'куб': cube, 'корень':sqrt, 'модуль':abs, 'синус':sin}
num = int(input())
command = input()

print(commands[command](num))
'''

# Интересная сортировка-1
'''
lst = [num for num in input().split()]
print(*sorted(lst, key=lambda str: sum([int(dig) for dig in str])))
'''
# Интересная сортировка-2
''''''
lst = sorted([int(num) for num in input().split()])
lst = [str(num) for num in lst]
print(*sorted(lst, key=lambda str: sum([int(dig) for dig in str])))
