# Больше предыдущего
'''
# Входные данные  1 5 2 4 3
# Ожидаемый выход   5   4  

# lst = [action for el in sequence]
lst = [i for i in input().split()]
# print(lst) # Получен список

# Решу задачу циклом

for el in range(1, len(lst)):
    if lst[el] > lst[el - 1]:
       print(lst[el])
'''

# Соседи одного знака
'''
# Ввод списка целых чисел с клавы
lst = [int(i) for i in input().split()] # -1 2 3 -1 -2 # 1 -3 4 -2 1

for el in range(1, len(lst)):
    if lst[el - 1] >= 0 and lst[el] >= 0: # Найдены отрицательные соседи
       print(lst[el - 1], lst[el])
       break
    elif lst[el - 1] < 0 and lst[el] < 0: # Найдены положительные соседи
       print(lst[el - 1], lst[el])
       break
'''


