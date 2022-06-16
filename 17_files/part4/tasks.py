# Конкатенация файлов
'''
count = int(input()) # 2
file_names = [] # file1.txt, file2.txt
for i in range(count):
    file_names.append(input())

# Создание файла output.txt
with open('output.txt', 'w', encoding='utf-8') as out_file:
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as con_file:
            out_file.writelines(con_file.readlines())
'''

# Лог файл
'''
# Создание файла с результатом анализа
with open('output.txt', 'w', encoding='utf-8') as out_file:
    # Чтение лог файла
    with open('logfile.txt', 'r', encoding='utf-8') as r_file:
        for line in r_file:
            name, enter_time, leave_time = line.strip().split(',')
            hours_dif = int(leave_time.split(':')[0]) - int(enter_time.split(':')[0])
            minutes_dif = int(leave_time.split(':')[1]) - int(enter_time.split(':')[1]) + hours_dif * 60
            if minutes_dif >= 60:
                out_file.write(f"{name}\n")
'''
