# Суммарная стоимость
'''
with open('ledger.txt', 'r', encoding='utf-8') as file:
    incomes = [int(price[1::]) for price in file.readlines()]
    print(f"${sum(incomes)}")
'''

# good students
'''
def greater_65(num):
    if int(num) >= 65:
        return True
    else:
        return False

# Вывести число студентов сдавших все 3 теста
good_students = 0
with open('grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if all(map(greater_65, line.split()[1::])):
            good_students += 1
print(good_students)
'''

# Самое длинное слово в файле
'''
# Читаю файл по строкам. 
# Превращаю строку в список 
# Определяю в ней длину максимального эл.
# Если макс. длина > текущей макс., то: обновляю макс. длину и очищаю список макс. слов
# Добавляю все эл, что имеют макс. длину из этой строки в список
# Если макс. длна = тек. макс., то добавляю все слова этой длины в список
# Продолжаю поиск по строкам
with open('words.txt', 'r', encoding='utf-8') as file:
    max_len = 0
    longest_words = []
    for line in file:
        if max_len < len(max(line.split(), key=len)):
            max_len = len(max(line.split(), key=len))
            longest_words.clear()
            longest_words.extend([word for word in line.split() if len(word) == max_len])
        elif max_len == len(max(line.split(), key=len)):
            longest_words.extend([word for word in line.split() if len(word) == max_len])
    print(*longest_words, sep="\n")
'''
# Более элегантное решение
# Здесь файл читается целиком 1 раз.
'''
with open('words.txt') as f:
    mylist = f.read().split()
    longest = max(map(len, mylist))
    print(*list(filter(lambda x: len(x) == longest, mylist)), sep='\n')
'''

# Tail of a file
'''
file_name = input()

with open(file_name, 'r', encoding='utf-8') as file:
    print(*file.read().split('\n')[-10:],sep='\n')
'''


# Пропущенные комментарии
'''
file_name = input() #code.py
uncommented_funcs = []

with open(file_name, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]

    for lineNum in range(len(lines)):
        if "def" in lines[lineNum] and "#" not in lines[lineNum-1]:
            uncommented_funcs.append(lines[lineNum][4:lines[lineNum].index('(')])

if len(uncommented_funcs) == 0:
    print("Best Programming Team")
else:
    print(*uncommented_funcs, sep="\n")
'''

# Транслитерация
''''''

d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
    }

with open('cyrillic.txt', 'r', encoding='utf-8') as inp_file, open('transliteration.txt', 'w', encoding='utf-8') as out_file:
    while inp_file.read(1):
        out_file.write(d.get(inp_file.read(1).lower(), inp_file.read(1)))
    

