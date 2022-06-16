# Задачки
'''
file_name = input() # file.txt

file = open(file_name)
file_data = file.read()
print(file_data)
file.close()
'''

# Чтобы гарантировать закрытие файла
'''
with open(input()) as f:
    print(f.read())
'''

# Вывод предпоследней строки
'''
with open(input()) as f:
    print(f.readlines()[-2])
'''

# Вывод случайной строки из файла

'''
import random

file = open("lines.txt", 'r', encoding='utf-8')
content = file.readlines()
rand = random.randint(0, len(content)-1) # Выбор строки для вывода
print(content[rand])
file.close()
'''

# Сумма чисел в файле (Числа на разных строках)

'''
file = open("numbers.txt", 'r', encoding='utf-8')
print(int(file.readline()) + int(file.readline()))
file.close()
'''

# Сумма чисел в файле (Числа на разных строках и между ними мусор в виде пробелов и \n)
'''
file = open("nums.txt", 'r', encoding='utf-8')
content = file.read().split()
print(int(content[0]) + int(content[1]))
file.close()
'''

# Общая стоимость
'''
file = open("prices.txt", "r", encoding='utf-8')
content = file.readlines()
# print(content) # Вся ценная информация находится после 1 \t и до \n
for index, str in enumerate(content):
    content[index] = str[str.find('\t')+1:str.find('\n'):1]
    content[index] = eval(content[index].replace('\t', '*')) # Выполняю перемножения
print(sum(content))
file.close()
'''

# tasks 2

