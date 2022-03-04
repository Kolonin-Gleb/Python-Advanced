# Входные данные  1 5 2 4 3
# Ожидаемый выход   5   4  

# lst = [action for el in sequence]
lst = [i for i in input().split()]
# print(lst) # Получен список

# Решу задачу циклом

for el in range(1, len(lst)):
    print(el)
    #if lst[el] > lst[el - 1]:
    #    print(el)

