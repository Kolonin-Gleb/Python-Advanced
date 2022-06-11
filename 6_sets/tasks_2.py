# Генераторы множеств и frozenset

# Уникальные слова (без пунктуации) в алфавитном порядке
# Мне необходимо удалить всю пунктуацию из строки = 

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
'''
for i in sentence:
   if i in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
       sentence = sentence.replace(i, "")

words = set()

for word in set(sentence.lower().split()):
    if len(word) < 4:
        words.add(word)

print(*sorted(words))
'''

# Файлы png в нижнем регистре, в алфавитном порядке через пробел.
'''
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
files = [file.lower() for file in files]
pngFiles = {file for file in files if '.png' in file}
print(*sorted(pngFiles))
'''
