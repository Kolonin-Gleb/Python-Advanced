# Parameters with default values have to be declared after parameters without default values

def print_sb(name, age = 18):
    print(f"Hello {name}")
    print(f"Your age is {age}")

# Параметры с значениями по умолчанию можно не указывать
# print_sb("Gleb")

# Параметры можно передавать по имени
# print_sb(age= 17, name="Leo")

'''
Символ * позволяет установить, какие параметры будут именнованными - 
то есть такие параметры, которым можно передать значения только по имени.
Все параметры, которые располагаются справа от символа *, получают значения только по имени:
'''
# age и company - именованные параметры
# def print_worker(name, *, age, company):
#     print(f"name = {name} age = {age} company = {company}")

# Нельзя указать age и company неявно
# print_worker("Neo", age=21, company="Microsoft")

'''
Параметры до / являются позиционными. Могут быть переданы только по позиции
'''
def print_hello_worker(name , /, age, company):
    print("Hello!")
    print(f"name = {name}, age = {age}, company = {company}")

# print_hello_worker("Jack",age=2, company="None")


'''
Функция может принимать неопределенное кол. параметров
'''
def print_sum(*nums):
    sum = 0
    for i in nums:
        sum += i
    print(sum)

print_sum(1, 2, 9, 2, 8, 4)

