# Вложенные словари и генераторы словарей

# Генератор словаря
'''
squares = {i: i**2 for i in range(6)}
print(squares)
'''

# Формирование словаря
# из словаря элементов
# заданными парами по ключам
'''
dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]

dict2 = {k: dict1[k] for k in selected_keys}

print(dict2)
'''

'''
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
result = {v: k for k, v in months.items()}
print(result)
'''

# Преобразование строки в словарь

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

s = s.split()
keys = []
values = []
for el in s:
    keys.append(int(el.split(':')[0]))
    values.append(el.split(':')[1])

result = dict(zip(keys, values))
print(result)
