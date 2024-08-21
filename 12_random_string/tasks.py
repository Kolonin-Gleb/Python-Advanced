# step 11
'''
from random import choice

n = int(input())

outcomes = ["Орел", "Решка"]

for i in range(n):
    print(choice(outcomes))

'''
# step 12
'''
from random import randint

n = int(input())

outcomes = [randint(1, 6) for _ in range(n)]

print(*outcomes, sep='\n')
'''

# step 13 Генератор паролей
'''
from random import choice

length = int(input())
password = ''
for i in range(length):
    password += choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(password)
'''

# Вычисление площади фигуры по системе неравенств используя метод Монте-Карло
# Задача 1
'''
import random
n = 10**6 # Кол. испытаний
k = 0     # Кол. исходов, когда все точки оказались внутри фигуры
s0 = 16   # Это площадь фигуры
for _ in range(n): # Перебор итераций
    # Описываем систему кодом 

    # Устанавливаем промежутки несстрогих неравенств
    x = random.uniform(-2, 2) # −2≤x≤2 # случайное число с плавающей точкой
    y = random.uniform(-2, 2) # −2≤y≤2 # случайное число с плавающей точкой

    # Оставшиеся неравенства в системе
    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2: # Если точчка с координатами попала в область
        k += 1
print((k/n)*s0)
'''

# Вычисление площади фигуры по системе неравенств используя метод Монте-Карло
# Задача 2 (Вычисление Pi)
'''
import random
n = 10**6       # количество испытаний
k = 0.0
for i in range(n):
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0)
print(4 * k / n)
'''

# Step 14 Лотерейный билет
'''
import random

numbers = set()
while len(numbers) != 7:
    numbers.add(random.randint(1, 49))

numbers = sorted(list(numbers))
print(*numbers, sep=' ')
'''

######################## Section 12.2 ########################

# Step 6 IP-adress
'''
from random import randrange
def generate_ip():
    return f'{randrange(256)}.{randrange(256)}.{randrange(256)}.{randrange(256)}'
# print(generate_ip())
'''

# Step 7 Лотерейный билет Латверии
'''
from string import digits, ascii_uppercase
from random import choice as c

def generate_index():
    d = digits
    l = ascii_uppercase
    return f"{c(l)}{c(l)}{c(d)}_{c(d)}{c(l)}{c(l)}"

# Мой вариант
# def generate_index():
#     return ''.join([*sample(string.ascii_uppercase, 2), str(randint(0, 99)), '_', *sample(string.ascii_uppercase, 2), str(randint(0, 99))])

print(generate_index())
'''

# Step 8 Перемешивание матрицы
'''
import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

rows = []
# Можно не менять элементы в списках
for row in range(len(matrix)):
    rows.append(matrix[row])

# Создаём новую матрицу перемешав её строки
matrix_2 = []

for row in range(len(matrix)):
    row = random.choice(rows)
    rows.remove(row) # Можно ли так удалить строку?
    matrix_2.append(row)

matrix = matrix_2 # Перемешивание завершено
'''

# Более простое решение
'''
import random
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)
print(matrix)
'''

# Step 9 - 100 уникальных лотерейных билетов
'''
from random import randint

tickets = set()

while len(tickets) != 100:
    tickets.add(randint(1000000, 9999999))

while tickets:
    print(tickets.pop())
'''

# Step 10 - Анаграмма 1
'''
from random import shuffle

word = list(input())
shuffle(word)
print(''.join(word))
'''

# Step 11
'''
from random import randint

nums = set(map(str, range(1, 76)))
matrix = []
for row in range(5):
    matrix.append([nums.pop(),nums.pop(),nums.pop(),nums.pop(),nums.pop()])
matrix[2][2] = '0'

for row in range(5):
    for col in range(5):
        print(matrix[row][col].ljust(3), end=' ')
    print() # Перенос строки
'''

# Step 12 Тайный друг
'''
from random import shuffle

n = int(input())

friends = []
for i in range(n):
    friends.append(input())
shuffle(friends)

for i in range(n):
    print(friends[i], '-', friends[i-1])
'''

# Step 13 Генератор паролей 1
'''
from random import *
from string import *

# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
def generate_password(length):
    s = list((ascii_letters + digits))
    [s.remove(c) for c in 'lI1oO0']
    return ''.join(sample(s, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep="\n")
'''

# Step 13 Генератор паролей 2
'''
import random

def generate_password(length):
    result = []
    digits = '23456789';
    small_letters = 'qwertyuipasdfghjkzxcvbnm';
    huge_letters = 'QWERTYUPASDFGHJKLZXCVBNM';
    s = "qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789"
    result += random.sample([elem for elem in digits], 1)
    result += random.sample([elem for elem in small_letters], 1)
    result += random.sample([elem for elem in huge_letters], 1)
    result += random.sample([elem for elem in s], length - 3)
    print(''.join(result))

def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)

n, m = int(input()), int(input())

generate_passwords(n, m)
'''
