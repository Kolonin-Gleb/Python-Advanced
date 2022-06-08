# ¬се возможные подсписки списка

lst = [el for el in input().split()]
print(lst) # a b v

# ѕодсписок длины 0
list_of_sublists = [[], ]

# ‘ормирование подсписков длин от 1 до длина самого списка - 1
sub_list_size = 1

while sub_list_size != len(lst):
	sub_lst = []
	for el in range(len(lst)): # ‘ормируем подсписки текущей длины.TODO: ¬озможно мне нужны циклы while, т.к. использу€ цикл for не получитс€ регулировать смещение?
		
		sub_lst.append(el)
		list_of_sublists.append(list(el))


# ѕодсписки произвольных длин от 2 до длина списка -1




# ѕодсписок максимальной длины = сам список
list_of_sublists.append(lst)

print(list_of_sublists) # [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]

