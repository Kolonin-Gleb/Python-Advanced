# step 11
'''
from random import choice

n = int(input())

outcomes = ["Орел", "Решка"]

for i in range(n):
    print(choice(outcomes))

'''
# step 12
'''
from random import randint

n = int(input())

outcomes = [randint(1, 6) for _ in range(n)]

print(*outcomes, sep='\n')
'''

# step 13 Генератор паролей
'''
from random import choice

length = int(input())
password = ''
for i in range(length):
    password += choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(password)
'''

