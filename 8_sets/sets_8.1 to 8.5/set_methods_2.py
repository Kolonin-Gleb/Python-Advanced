# Способы удалить эл. из множества

colors = {'Yellow', 'Orange', 'Black'}

print(colors)

# colors.clear(Orange) - метод clear не принимает аргументов -

# colors.discard('Orange') # - исключение эл. при его наличии +

# colors.remove('Orange') # удаление эл. или ошибка +

# colors.pop('Orange') # pop удалит последний эл. (в случае с множествами - случайный)
# нельзя явно задать, какой эл. удалить. -

# del colors['Orange'] # Из множеств нельзя удалять эл.
# исп. кл. слово del
 
print(colors)

# Из списка можно удалять эл. исп. del.
# Тем не менее, делать это нужно по индексу эл.
# colours = ['white', 'grey', 'magenta']
# del colours[1]
# print(colours)


myset = set('python')

item = myset.pop()
print(item, len(myset))

