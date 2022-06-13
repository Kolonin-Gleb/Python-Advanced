# questions
'''
def display(**kwargs):
    for v in kwargs.values():
        print(v, end=' ')

display(emp='Kelly', salary=9000)
'''

'''
def outer_func(a, b):
    def inner_func(c, d):
        return c + d + a*b
    return inner_func

res = outer_func(5, 10)(3, 2) # outer_func вернёт функцию, которая будет вызвана с аргументами 2 ()
print(res)
'''

'''
data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
result = list(map(lambda x: '.'.join(x), data)) # Происходит соединение через .
print(result[1])
'''

'''
from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers) # База не указана, поэтому за неё берётся 1 эл. последовательности
# Все элементы будут просуммированы 1+2+3 = 5 и к ним будет + база, т.е. 5+1 = 6
print(result)
'''

'''
from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda a, b: a * b, numbers, 10)
# Все элементы будут * 1*2*3=6 и будут умножены на базу 6*10=60
print(result)
'''

'''
from functools import reduce
import operator

def flatten(data):
    return reduce(operator.concat, data, [])

result = flatten([[1, 2], [3, 4], [], [5]])

print(result)
'''

#tasks
# Письмо для экзамена
'''
def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f"To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!"
'''

'''
def concat(*args, sep=' '):
    args1 = []
    args1.append(args)
    return list(map(sep.join, args1))[0]

print(concat('hello', 'python', 'and', 'stepik', sep='*'))

# Более элегантно
def concat(*elems, sep = ' '):
    return sep.join([str(elem) for elem in elems])
'''
