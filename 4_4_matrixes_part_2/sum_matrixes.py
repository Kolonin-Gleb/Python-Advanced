# Сложение матриц

# Установка размера матриц
n, m = input().split()

n = int(n)
m = int(m)

# Ввод двух матриц

mat1 = []
mat2 = []

for row in range(n):
    mat1.append( [int(i) for i in input().split()] )

input() # Заглушка

for row in range(n):
    mat2.append( [int(i) for i in input().split()])

# Сложение заданных матриц.
# Для экономии ресурсов буду сразу выводить результат сложения

for row in range(n):
    for col in range(m):
        print( (mat1[row][col] + mat2[row][col]), end=" ")
    print()


