# Деление элементов списка на подсписки
# Буду формировать все подсписки сразу, т.к. это позволит сделать их нужного размера и не выйти за рамки
'''
lst = [i for i in input().split()]
length = int(input())

# Создание списка содержащего заданное число подсписков
lst_of_sublists = []
for i in range(length):
    lst_of_sublists.append([])

# Размещение элементов списка по подспискам
cur_el = 0
while cur_el < len(lst): # Добавляем элементы
    for sub_lst_num in range(length): # Идём по подспискам
        lst_of_sublists[sub_lst_num].append(lst[cur_el])
        cur_el += 1
        if not cur_el < len(lst):
            break

print(lst_of_sublists)
'''

# Максимальный в области под побочной диагональную включительно
'''
size = int(input())
# Построчный ввод матрицы
matrix = []
for i in range(size):
    matrix.append([int(i) for i in input().split()])

# print(matrix)
# Для удобства поиска буду идти справа налево, сверху вниз

maximum = -999

for rowNum in range(size): # Иду по каждой строке матрицы
    elements_to_check = rowNum + 1 # +1 т.к. нумерация стрко идёт с 0
    row_to_check = matrix[rowNum][::-1]
    row_to_check = row_to_check[0:elements_to_check:1]
    row_max = max(row_to_check)
    if row_max > maximum:
        maximum = row_max
    
print(maximum)
'''

# Снежинка
'''
from math import floor

size = int(input())
# Создание шаблона
matrix = ['.'] * size
for i in range(size):
    matrix[i] = ['.'] * size

# Заполнение диагоналей
for i in range(size):
    matrix[i][i] = '*'

for row in range(size-1, -1, -1):
    matrix[row][size-1 - row] = '*'

# Заполнение вертикали и горизонтали
col = floor(size / 2)
for row in range(size):
    matrix[row][col] = '*'
    matrix[col][row] = '*'

for row in range(len(matrix)):
    print(*matrix[row])
'''

