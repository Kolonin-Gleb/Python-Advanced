import re # Необходимо вывести номера всех строк, удовлетворяющих рег. выражению .*a.*n.*t.*o.*n
suspects = [input() for _ in range(int(input()))]
for number, suspect in enumerate(suspects, 1):
    if re.match('.*a.*n.*t.*o.*n', suspect): print(number, end=' ')

