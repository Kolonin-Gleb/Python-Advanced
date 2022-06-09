# Проверка матрицы на симметричность от основной диагонали
# '''
# Я полагаю, что матрицу следует хранить как список списков,
# где каждый вложенный список - строка матрицы
# '''

# # Матрица является симметричной относительно основной диагонали если она = транспонированной версии

# size = int(input())
# matrix = []

# # Ввод строк матрицы
# for row in range(size): 
#     matrix.append([int(el) for el in input().split()])
# # Транспонированная матрица
# t_matrix = [list(x) for x in zip(*matrix)]
# '''
# print(matrix)
# print("\n\n")
# print(t_matrix)

# print("___________")
# '''
# if matrix == t_matrix:
#     print("YES")
# else:
#     print("NO")

# Отражение матрицы по горизонтальной оси ---

from math import ceil

size = int(input())
matrix = []

# Ввод строк матрицы
for row in range(size): 
    matrix.append([int(el) for el in input().split()])

# Теперь нужно отразить по гор. оси ---

# Определяю сколько строк снизу поставить наверх: # Нужно округлять в большую сторону
rows_to_reflect = ceil(size / 2) # Кол. строк, что нужно взять снизу и поставить наверх

r_matrix = []

# Перетаскивание нижних строк наверх
for i in range(1, rows_to_reflect + 1):
    r_matrix.append(matrix[-i])

# Перетаскивание оставшихся верхних строк вниз Идём синзу вверх
for i in range(size - rows_to_reflect, 0, -1):
    r_matrix.append(matrix[i-1])

# print("\n\n")
# for row in range(size):
#     print(*matrix[row])
# print("\n\n")
for row in range(size):
    print(*r_matrix[row])

