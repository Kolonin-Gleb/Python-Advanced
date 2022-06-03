'''
# Именованные аргументы следует применять, когда функция принимает > 3 аргументов.
# Это повышает удобочитаемость кода

# При использовании именованных аргументов не отбивай = пробелами

def make_circle(x, y, radius, line_width, fill):
    print(x, y, radius, line_width, fill)

# make_circle(x=10, y=5, radius=17, line_width=2.5, fill=True)


# Необязательные аргументы. Их значение по умолчанию указывается через =

def make_square(x, y, side_length, line_width, fill=True):
    print(x, y, side_length, line_width, fill)

# make_square(x=10, y=5, side_length=20, line_width=2.5)

def my_func(x, y):
    print(x, y)

my_func(10, 2)
'''

def matrix(n=1, m=1, value=0):
    mult = []

