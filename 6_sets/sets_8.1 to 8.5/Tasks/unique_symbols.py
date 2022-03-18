n = int(input())
words = ''

# Созранение слов
for _ in range(n):
    words += input().lower()

# Вывод уникальных символов в словах
print(len(set(words)))

