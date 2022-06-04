# встроенные функции map(), filter(), reduce()
'''
def increase(num):
    return num + 7


numbers = [1, 2, 3, 4, 5, 6]
new_numbers = map(increase, numbers) #  используем встроенную функцию map()

print(new_numbers) # Получаю особенный объект (итератор)


for num in new_numbers: #  итерируем циклом for
    print(num)
'''

'''
iterable = [1, 2, 3]
result = list(map(len, iterable))
print(result)
'''

random_list = [1, 'a', 0, False, True, '0', 7, '']
filtered_list = list(filter(None, random_list))
print(filtered_list)