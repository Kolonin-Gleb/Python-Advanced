# В задании работа ведётся искл. с квадратными матрицами
matrix_size = int(input())

el_bigger_avg_in_rows = [0] * matrix_size

for row in range(matrix_size):
    matrix_row = [int(i) for i in input().split()]
    avg_of_matrix_row = (sum(matrix_row) / matrix_size)
    # Подсчёт кол. эл. больших ср. ар. в каждой строке
    for col in range(matrix_size):
        if matrix_row[col] > avg_of_matrix_row:
            el_bigger_avg_in_rows[row] += 1
    
# Вывод кол. эл. больших ср. ар. в каждой строке
for el in el_bigger_avg_in_rows:
    print(el)

