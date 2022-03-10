# matrix n*n
'''
n = int(input())

matrix = []

# matrix input
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

# counting matrix trace
trace = 0
for i in range(n):
    trace += matrix[i][i]

print(trace)
'''

# Решение без создания матрицы
'''
trace = 0
for i in range(int(input())):
     value = int(input().split()[i]) # Здесь происходит взятие i элемента из сформированного списка
     trace += value
print(trace)
'''
