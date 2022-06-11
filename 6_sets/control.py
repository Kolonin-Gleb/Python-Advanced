# Домашнее задание
'''
n = int(input()) # всего учеников
m = int(input()) # съела собака
k = int(input()) # выкл. свет
p = int(input()) # собака + свет

print(n - (m + k - p))
'''
# Восход
'''
sunrise = input().split()
print(len(sunrise) - len(set(sunrise)))
'''
# Города
'''
count = int(input())
cities = set()
for i in range(count+1):
    cities.add(input())
if len(cities) == count+1: print("OK")
else: print("REPEAT")
'''
# Книги на прочтение
'''
m = int(input())
n = int(input())
home_books = []
books_to_read =[]
for i in range(m):
    home_books.append(input())
for j in range(n):
    books_to_read.append(input())

for book in books_to_read:
    if book in home_books:
        print('YES')
    else:
        print('NO')
'''
# Странное увлечение
'''
set1 = set(input().split())
set2 = set(input().split())

if len(set1.intersection(set2)) == 0:
    print("BAD DAY")
else:
    print(*sorted(set1.intersection(set2), key=int, reverse=True))
'''
# Онлайн школа BeeGeek
''''''
m = int(input())
always_on_lesson = set()
# Определение тех, кто был на 1 паре
n = int(input())
for j in range(n):
    always_on_lesson.add(input())

m -=1

for i in range(m):
    n = int(input())
    visited = set()
    for j in range(n):
        visited.add(input())
    always_on_lesson.intersection_update(visited)

print(*sorted(always_on_lesson),sep='\n')