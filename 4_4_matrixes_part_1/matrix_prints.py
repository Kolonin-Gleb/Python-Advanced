n, m = int(input()), int(input())
# n - строки m - столбцы

matrix = []

for row in range(n):
    matrix.append([0] * m) # Добавление строк в матрицу
    for col in range(m): # Заполнение столбцов строки
        matrix[row][col] = input()

# Вывод матрицы по строкам
for row in range(n):
    for col in range(m):
        print(matrix[row][col], end=" ")
    print()

print()

# Вывод матрицы по столбцам
for col in range(m):
    for row in range(n):
        print(matrix[row][col], end=" ")
    print()


