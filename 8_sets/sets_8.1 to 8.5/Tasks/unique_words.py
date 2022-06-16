# общее количество различных слов в строке без учета регистра.

text = input().lower()

# Удаление ненужных символов
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace(':', '')
text = text.replace(';', '')
text = text.replace('-', '')
text = text.replace('?', '')
text = text.replace('!', '')
# Можно было бы заменить на рег. выражение

words = set(text.split())

print(words)
print(len(words))


