# lst = [i for i in input().split()]

# # Если элементов нечетное число, то последний элемент
# # остается на своем месте.
# # Пример: из 3х эл. местами обменяются первые 2

# if len(lst) % 2 == 1:
#     length = len(lst) - 1 # ЧТобы не трогать последний эл. без пары
# else:
#     length = len(lst)

# for i in range(1, length, 2): # start, stop, step
#     lst[i - 1], lst[i] = lst[i], lst[i - 1]

# print(lst) # Ответ нужно дать в формате строки, а не списка

lst = [int(i) for i in input().split()]

print(lst)

lst[lst.index(min(lst))], lst[lst.index(max(lst))] = lst[lst.index(max(lst))], lst[lst.index(min(lst))]

print(lst)

# Конвертация списка целых чисел в строку

# strLst = [str(i) for i in lst]
# str = ' '.join(strLst)
# print(str)
