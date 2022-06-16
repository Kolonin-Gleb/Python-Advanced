'''
lst = [int(num) for num in input().split()]
set1 = set()
set_size = 0

for el in lst:
    set1.add(el)
    if set_size == len(set1):
        print("YES")
    else:
        print("NO")
        set_size += 1
'''
# Более элегантно
'''
s = set()
for item in input().split():
    print(["NO", "YES"][int(item) in s])
    s.add(int(item))
'''

'''
n = int(input())
intersection_res = set(input())
for i in range(1, n):
    intersection_res.intersection_update(set(input()))
intersection_res = [int(num) for num in intersection_res]
print(*sorted(intersection_res))
'''
# Более элегантное решение
'''
n = int(input())
numbers = [input() for _ in range(n)]

num_set = set(numbers[0]).intersection(*numbers)
print(*sorted(num_set))
'''

# Книги на прочтение

'''
n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())
onlyOneBook = 2*(x + y + z) - 3*(n+m+k) + 3*t
twoBooks = 2*(n+m+k) - x - y - z - 3*t
noBooks = a + n + m + k - x - y - z - t

print(onlyOneBook)
print(twoBooks)
print(noBooks)
'''

'''
# Множество является изменяемым типом данных, но его элементы должны быть неизменяемыми.
# Множество не может содержать множество или список

a = dict(One=1, Two=2)
print(a)
set1 = {1, 2}
# множество не может содержать множество
'''

# Методы множеств часть 3

# Метод isdisjoint() - для проверки отсутствия / наличия общих элементов
''''''
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7}
set3 = {7, 8, 9}

print(set1.isdisjoint(set2)) # False
print(set1.isdisjoint(set3)) # True
print(set2.isdisjoint(set3)) # False

