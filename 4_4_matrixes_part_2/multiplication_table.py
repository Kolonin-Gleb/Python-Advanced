n, m = int(input()), int(input())

mult = []

for row in range(n):
    # Добавление пустой строки
    mult.append([0] * m)
    for col in range(m):
        # Заполнение строки
        mult[row][col] = str(row * col)

# Вывод матрицы
for row in range(n):
    for col in range(m):
        print(mult[row][col].ljust(3), end=" ")
    print()

