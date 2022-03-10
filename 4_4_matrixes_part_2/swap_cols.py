rows = int(input())
cols = int(input())

matrix = []

# Заполнение данных
for _ in range(rows):
    row = input()
    matrix.append( [int(num) for num in row.split()] ) # Можно ввести больше эл. чем разрещает кол. столбцов.

# print("\n\nВаша матрица:")
# Вывод матрицы по строкам
for row in range(rows):
    for col in range(cols):
        print(matrix[row][col], end=" ")
    print()


# Столбцы, что нужно поменять местами
# print("\nВведите индексы столбцов, что нужно поменять местами через пробел:")
col1, col2 = input().split()

col1 = int(col1)
col2 = int(col2)

# Пока в матрице есть строки
# Буду идти по матрице и осуществлять обмен элементов в соотв. столбцах
for row in range(rows):
    matrix[row][col1], matrix[row][col2] = matrix[row][col2], matrix[row][col1]

# print("\n\nВаша матрица после перестановки столбцов:")
# Вывод матрицы по строкам
for row in range(rows):
    for col in range(cols):
        print(matrix[row][col], end=" ")
    print()

