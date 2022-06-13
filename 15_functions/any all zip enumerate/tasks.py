# Небольшое повторение

# Функции all() и any() в связке с функцией map()
# Могут быть полезны, когда необходимо проверить набор данных на удовлетворение условию
'''

numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
result = all(map(lambda x: True if x > 10 else False, numbers))
'''
# Функция zip - объединяет элементы из полученных коллекций в кортежи
'''
numbers = [1, 2, 3]
words = ['one', 'two', 'three']
nums = [-1, -2, -3]

# for pair in zip(numbers, words, nums):
#     print(pair)

# Создание словаря с помощью zip из нескольких наборов данных

dict1 = dict(zip(numbers, words))
print(dict1)
'''

# step 11 correct ip
'''
# Напишите программу с использованием встроенной функции all()

print(all(x.isdigit() and int(x) < 256 for x in input().split('.')))

user_adress = input().split('.')
user_adress = list(map(lambda part: part if part.isdigit() else '999', user_adress))
user = list(map(lambda part: True if (int(part) <= 255) else False, user_adress))
print(all(user))
'''

# Интересные числа
'''
Напишите программу с использованием встроенной функции all() для обнаружения всех целых чисел
в диапазоне [a;b], 
которые делятся на каждую содержащуюся в них цифру без остатка. - вот тут-то и пригодится all()

a = int(input())
b = int(input())

def is_devided_by_digits(number):
    number = str(number)
    for dig in number:
        if int(number) % int(dig) != 0:
            return False
    return True

lst = [num for num in range(a, b+1) if not '0' in str(num)] # В числах не должно быть 0, т.к. / 0 - ошибка

result = [num for num in lst if is_devided_by_digits(num)]

print(*result)
'''
# Более элегантное решение
'''
def check(num):
    return all(map(lambda x: int(x) and num % int(x) == 0, str(num))) # Число преобразуется в строку. x - символ числа
    # Если x = '0', то преобразование int(x) будет трактоваться как False и num не пройдёт!

a, b = int(input()), int(input())
seq = range(a, b + 1)
print(*list(filter(lambda x: check(x), seq))) # Фильтруем значения последовательности, по условию
'''

# Хороший пароль
'''
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, 
содержит хотя бы одну цифру, заглавную и строчную букву. 
Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

password = input()

def predicate(password):
    if len(password) < 7:
        return False
    result = [False, False, False]
    for sym in password:
        if sym.islower():
            result[0] = True
        if sym.isdigit():
            result[1] = True
        if sym.isupper():
            result[2] = True
    return all(result)
       
print('YES' if predicate(password) else 'NO')
'''

# Отличники

classes = int(input())
a_students = [0]*classes

for i in range(classes):
    students = int(input())
    for j in range(students):
        if input().split()[1] == '5':
            a_students[i] += 1

print(("NO", "YES")[all(a_students)])
