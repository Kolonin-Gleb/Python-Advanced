# Упаковка дубликатов
'''
letters = [letter for letter in input().split()] # Буквы
letters_packed = [[letters[0]]] # упакованные дубликаты # БАЗА, чтобы работало

for letter in range(len(letters)): # Идём по всем буквам
    if letters[letter] in letters_packed[-1][-1]: # Буква совпадает с набираемой группой
        letters_packed[-1].append(letters[letter])
    else: # Добавляем новую группу с этой буквой
        letters_packed.append(list(letters[letter]))

del letters_packed[0][0] # Удаляю костыль-базу

print(letters_packed)

'''

# Более элегантное решение
'''
packed = []
lst = input().split()
for i in lst:
    packed.append([i]) if not packed or i not in packed[-1] else packed[-1].append(i)
print(packed)
'''

# Разбиение на чанки
''' 
lst = [el for el in input().split()]
chunk_size = int(input())
j = 0
chunks = [[]]
for elem in lst:
    if j < chunk_size: # по размеру чанка
        chunks[-1].append(elem)
        j += 1
    else:
        chunks.append(list(elem))
        j = 1
print(chunks)
'''

# Все возможные подсписки списка
'''
lst = [el for el in input().split()]
sublist_size = 1
list_of_sublists = [[], []]

pos = 0 # Позиция с которой нужно начинать формировать подсписки
cur_pos = 0 # Текущая позиция эл, что мы добавляем

while sublist_size != len(lst):
    while cur_pos < len(lst):
        if len(list_of_sublists[-1]) < sublist_size: # Сборка подсписка нужной длины
            list_of_sublists[-1].append(lst[cur_pos])
            cur_pos += 1
        else:
            list_of_sublists.append([]) # Список для будущего заполнения
            pos += 1
            cur_pos = pos
            
    sublist_size += 1
    pos = 0
    cur_pos = 0
    list_of_sublists.append([]) # Список для будущего заполнения

list_of_sublists[-1].extend(lst)
print(list_of_sublists)
'''

# Более элегантное решение, которое я не понимаю!
input_data = input().split()
output_data = [[]]
for i in range(len(input_data)): # Сборка подсписка нужной длины
    for j in range(len(input_data) - i): # j - позиция начиная с которой формируется вложенный список
        output_data.append(input_data[j: j + i + 1])
print(output_data)
