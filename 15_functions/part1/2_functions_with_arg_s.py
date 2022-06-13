# Переменное количество аргументов
'''
def my_func(*args):
    print(type(args))
    print(args)

my_func()
my_func(1, 2, 3)
my_func('a', 'b')
'''

# Передача именованных аргументов в форме словаря
'''
def my_func2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])

info = {'name':'Gleb', 'age':'17', 'job':'unemployed'}

# my_func2(**info)
'''

# keyword-only аргументы. Для вызова функции, только передавая аргументы по именам
# * - разделитель между обычными аргументами и строго именованными
'''
def make_circle(x, y, radius, *, line_width=1, fill=True):
    print(f'x = {x} y = {y} radius = {radius} line_width = {line_width} fill = {fill}')

make_circle(1, 2, 3, line_width=4, fill=False)
make_circle(1, 2, 3, 4, False) - error!
'''

# Подсчёт числа аргументов
'''
def count_args(*args):
    return len(args)

count_args(1, 2, 3)
'''

# Сумма квадратов аргументов
'''
def sq_sum(*args):
    sum_of_squares = 0
    for i in args:
        sum_of_squares += i*i
    return sum_of_squares

print(sq_sum(1, 2, 3))
'''

# Подсчёт среднего ар. среди int и float аргументов
'''
def mean(*args):
    sum = 0
    counter = 0
    for i in args:
        if isinstance(i, int) and type(i) != bool or isinstance(i, float):
            sum += i
            counter += 1
    
    if counter == 0:
        return 0.0
    else:
        return sum / counter

print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
'''

# Приветствие
'''
def greet(name, *args):
    greeting = f'Hello, {name}'
    for i in args:
        greeting += f' and {i}'
    greeting += '!'
    return greeting

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
'''

# Отсортированный по алфавиту вывод именнованных аргументов
'''
# def info_kwargs(**kwargs):
#     keys = list(kwargs.keys())
#     keys.sort()
#     for key in keys:
#         print(f"{key}: {kwargs[key]}")

def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f'{k}: {v}')

info_kwargs(first_name='Gleb', last_name='Kolonin', age=17, job='student')
'''

# Вывод продуктов
'''
def print_products(*args):
    counter = 0
    for i in args:
        if isinstance(i, str) and i != '':
            counter+=1
            print(f"{counter}) {i}")
    if counter == 0:
        print("Нет продуктов")
'''

# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# 1) Бананы
# 2) Яблоки
# 3) Макароны
# print_products([4], {}, 1, 2, {'Beegeek'}, '')
# Нет продуктов



# Произовльное число аргументов. Будет получен кортеж
def func1(*args):
    print(type(args))
    print(args)

# Произвольное число именнованных аргументов. Будет получен словарь
def func2(**kwargs):
    print(type(kwargs))
    print(kwargs)

func1(1, 2 , 3, 4, 5)
func2(a1='1', a2='2', a3='3', a4='4', a5='5')
