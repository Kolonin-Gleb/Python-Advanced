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

