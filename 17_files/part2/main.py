# Переворот строки
'''
with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.readline()[::-1])
'''

# Все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.
'''
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()[::-1]
    print(*content, sep='')
'''

# Длинные строки
'''
# Прочитаю весь файл в список строк. 
# Определю макс. длину.
# Выведу те строки из списка, что = определенной длине

with open('lines.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()] # Удаление символов \n
    # print(lines)
    length = len(max(lines, key=len))

    for line in lines:
        if len(line) == length:
            print(line)
'''

# Сумма чисел в строках
'''
with open('numbers.txt', 'r', encoding='utf-8') as f:
    lines = [line.split() for line in f.readlines()]
    for line in lines:
        sum = 0
        for digit in line:
            sum += int(digit)
        print(sum)

with open('numbers.txt') as f:
    for line in f:
        print(sum(map(int, line.split())))
'''

