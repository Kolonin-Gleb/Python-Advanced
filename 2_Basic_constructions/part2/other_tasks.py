# Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы одним пробелом.
'''
digits = [int(digit) for digit in input().split()]

digits_moved = []
digits_moved.append(digits[-1])

for i in range(len(digits)-1):
    digits_moved.append(digits[i])

print(*digits_moved)


a = input().split()
print(*([a[-1]] + a[:-1]))
'''

# программу для подсчета количества разных элементов в списке.
'''
unique = []

lst = input().split()

for i in lst:
    if not i in unique:
        unique.append(i)

print(len(unique))
'''

# Произведение или нет?
'''
count = int(input())
digits = []

for i in range(count):
    digits.append(int(input()))

guess = int(input())

for i in range(count): # Идём по всем числам
    for j in range(count): # Пробую делить на все числа
        if digits[j] == 0: continue
        res = guess // digits[j]
        if res == digits[j]:
            # res должен присутствовать 2 раза
            if digits.count(res) >= 2:
                print("ДА")
                exit()
            else:
                print("НЕТ")
                exit()
        elif res in digits: # res должен присутствовать
            print("ДА")
            exit()
print("НЕТ")
'''

# Макс. решек подряд
'''
str = input()
maximum = 0
current = 0
for letter in str:
    if letter == 'Р':
        current += 1
    else:
        if maximum < current: maximum = current
        current = 0

if maximum < current: maximum = current
print(maximum)
'''

