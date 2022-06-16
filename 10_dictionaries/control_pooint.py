'''
d = {('foo', 100), ('bar', 200), ('baz', 300)}
print(type(d))
print(d)
'''

# task 1
'''
Дополните приведенный код, чтобы в списках значений элементов словаря my_dict 
не было чисел, больших 20. При этом порядок оставшихся элементов меняться не должен.
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

for k in my_dict:
    my_dict[k] = [num for num in my_dict[k] if num <=20] 
# print(my_dict)
'''

# task 2
'''
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

full_emails = []

for k in emails:
    full_emails.extend( [f"{name}@{k}" for name in emails[k]] )

print(*sorted(full_emails), sep="\n")
'''
# ДНК
'''
dnk = input()
# Превращение в РНК
dnk = dnk.replace("A", "u")
dnk = dnk.replace("C", "g")
dnk = dnk.replace("T", "a")
dnk = dnk.replace("G", "c")
print(dnk.upper())
'''

# Порядковый номер
'''
words = input().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# С конца в начало
sequence = []
for word in words[::-1]:
    sequence.append(frequency[word])
    frequency[word] -= 1

print(*sequence[::-1])
# прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
# 1 1 2 1 1 2 1 2 3 1
'''

# Scrabble game
''''''

prices = {
    1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'], 8: ['J', 'X'],
    10: ['Q', 'Z']
}

letters = [letter for letter in input()]
price = 0
for letter in letters:
    for k in prices:
        if letter in prices[k]:
            price += k
            break

print(price)
