# Модуль fraction
'''
Тип данных Fraction представляет обыкновенную дробь с заданным числителем и знаменателем
'''

# Создание Fraction
'''
from fractions import Fraction
num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')

print(num1, num2, num3, sep='\n')
'''
# Создавать числа Fraction нужно из int или str типов данных. При float будут ошибки

# tasks

# from fractions import Fraction as F
'''
numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
frs = [F(num) for num in numbers]
for b in range(len(numbers)):
    print(f"{numbers[b]} = {frs[b]}")

s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
s = [F(dig) for dig in s.split()]
print(max(s) + min(s))

m = int(input())
n = int(input())
print(F(m , n))

num1 = (input())
num2 = (input())
print(f"{num1} + {num2} = {F(num1) + F(num2)}")
print(f"{num1} - {num2} = {F(num1) - F(num2)}")
print(f"{num1} * {num2} = {F(num1) * F(num2)}")
print(f"{num1} / {num2} = {F(num1) / F(num2)}")
'''

# Сумма дробей до n
'''
from fractions import Fraction as F
n = int(input())
sum = 0
dig = 1
while dig <= n:
    sum += F(1, dig*dig)
    dig+=1
print(sum)
'''

# Упорядоченные НЕсократимые дроби
# знаменатель которых не превосходит n.
from fractions import Fraction as F

n = int(input())
numerator = 1 # числитель
denominator = n # знаменатель
ans = set()

while denominator != 0: # Буду генерировать сначала все дроби, с максимальным знаменателем с меньшим
    while numerator < denominator:
        ans.add(F(numerator, denominator))
        numerator += 1
    numerator = 1
    denominator -= 1

print(*sorted(list(ans)), sep="\n")

'''
Подсказка, gcd нужен для устранения дублей при сокращении дроби... А какой тип коллекций питона не содержит дублей? 
Правильно - set
Попробуйте использовать множество для хранения результатов
'''
# Исходя из подсказки и того факта, что дроби должны быть упорядочены я делаю вывод, что 
# мне следует сначала сформировать все дроби, затем отсортировать и вывести
