# step 2
'''
lst = input().split()
lst = [int(x) for x in lst]

# print(lst)

bigger_than_previous = 0

for i in range(1, len(lst)):
    if lst[i - 1] < lst[i]:
        bigger_than_previous += 1

print(bigger_than_previous)
'''

# step 3
'''
lst = input().split()
lst = [int(x) for x in lst]

for i in range(1, len(lst), 2):
    lst[i - 1], lst[i] = lst[i], lst[i - 1]


for i in range(len(lst)):
    print(lst[i], end=' ')
'''

# step 4
''''''
lst = input().split()
lst = [int(x) for x in lst]

lst[0], lst[-1]

for i in range(1, len(lst)):
    lst[i - 1], lst[i] = lst[i], lst[i - 1]


for i in range(len(lst)):
    print(lst[i], end=' ')
