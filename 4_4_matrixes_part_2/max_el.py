rows, cols = int(input()), int(input())

# Заполнение матрицы с клавиатуры

matrix = []

for _ in range(rows):
    row = input()
    matrix.append( [int(num) for num in row.split()] ) # Можно ввести больше эл. чем разрещает кол. столбцов.
# print(matrix)


# Поиск первого максимального элемента

max_el = -9999999999
max_el_row_position = -1
max_el_col_position = -1

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > max_el:
            max_el = matrix[i][j]
            max_el_row_position = i
            max_el_col_position = j

# print(max_el) # Для моей проверки
print(max_el_row_position, max_el_col_position)

