# Сохранение строки в файл
'''
str = input()

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(str)
'''

# Случайные числа
'''
# Напишите программу, записывающую в текстовый файл random.txt 
# 25 случайных чисел в диапазоне от 111 до 777 (включительно), каждое с новой строки.

from random import randint

# Формирование списка случайных чисел
rands = [str(randint(111, 777))+'\n' for i in range(25) ]
# print(rands)

with open('random.txt', 'w', encoding='utf-8') as f:
    f.writelines(rands)
'''

# Тоже самое с использованием print
'''
from random import randint
rands = [str(randint(111, 777))+'\n' for i in range(25) ]

with open('random.txt', 'w', encoding='utf-8') as f:
    print(*rands, sep='', file=f)
'''

# Создание копии файла с нумерацией строк
'''
with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('output.txt', 'w', encoding='utf-8') as f:
    for number, line in enumerate(lines, 1):
        f.write(f"{str(number)}) {line}")
'''

# Подарок на новый год
'''
with open('class_scores.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]

    # Делю на 2 списка
    names = []
    scores = []
    for line in lines:
        names.append(line.split()[0])
        scores.append(int(line.split()[1]))

# Баллов не должно быть > 100
with open('new_scores.txt', 'w', encoding='utf-8') as f:
    # Даю всем кому можно 5 баллов
    scores = list(map(lambda num: 100 if num >= 95 else num+5, scores))
    # Собираю данные из списков через zip
    for name, score in zip(names, scores):
        f.write(f'{name} {score}\n')
'''
# Более элегантное решение
with open('class_scores.txt', 'r', encoding='utf-8') as class_scores, open('new_scores.txt', 'w', encoding='utf-8') as new_scores:
    for line in class_scores:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=new_scores)

# 
