# Сумма чисел в файле
'''
# Решение через рег. выражения
import re

with open('nums.txt', 'r', encoding='utf-8') as f:
    my_list = [re.findall(r'\d+', line) for line in f.readlines()]
    # print(my_list)
    summa = 0
    for numbers in my_list:
        for num in numbers:
            summa += int(num)
    print(summa)
'''
'''
# Более элегантное решение
import re
with open('nums.txt') as f:
    print(sum(map(int, re.findall(r'\d+', f.read()))))
'''
# Статистика по файлу
'''
with open('file.txt', 'r', encoding='utf-8') as f:
    lines_lst = [line.strip() for line in f.readlines()]
    lines = len(lines_lst)
    words = 0
    letters = 0

    for line in lines_lst:
        print(line)
        words += len(line.split())
        for sym in line:
            if sym.isalpha():
                letters += 1

    print("Input file contains:")
    print(f"{letters} letters")
    print(f"{words} words")
    print(f"{lines} lines")
'''

# Random name and surname
'''
from random import choice
# Открытие сразу 2х файлов
with open('first_names.txt') as f_names, open('last_names.txt') as l_names:
    fnames = [fname.strip() for fname in f_names.readlines()]
    lnames = [lname.strip() for lname in l_names.readlines()]
    print(choice(fnames), choice(lnames))
    print(choice(fnames), choice(lnames))
    print(choice(fnames), choice(lnames))
'''

# Необычные страны. Выборка из текстового файла
'''
with open('population.txt') as f:
    data = [line.strip() for line in f.readlines()]
    for country in data:
        if country[0] == 'G':
            name, population = country.split('\t')
            if int(population) > 500_000:
                print(name)
'''

# Список словарей из csv файла
# csv файл можно обрабатывать, как обычный текстовый файл.
# Его значения разделены через ,
'''
def read_csv():
    with open('data.csv') as f:
        keys = f.readline().strip().split(',')
        values = [line.strip() for line in f.readlines()] # Список, где каждый элемент - строка значений
        data_dict = []
        for line in values:
            data_dict.append(dict(zip(keys, line.split(','))))
        return data_dict

print(read_csv())

policyID,statecode,county,eq_site_limit,hu_site_limit,fl_site_limit,fr_site_limit,tiv_2011,tiv_2012,eq_site_deductible,hu_site_deductible,fl_site_deductible,fr_site_deductible,point_latitude,point_longitude,line,construction,point_granularity
119736,FL,CLAY COUNTY,498960,498960,498960,498960,498960,792148.9,0,9979.2,0,0,30.102261,-81.711777,Residential,Masonry,1
448094,FL,CLAY COUNTY,1322376.3,1322376.3,1322376.3,1322376.3,1322376.3,1438163.57,0,0,0,0,30.063936,-81.707664,Residential,Masonry,3
206893,FL,CLAY COUNTY,190724.4,190724.4,190724.4,190724.4,190724.4,192476.78,0,0,0,0,30.089579,-81.700455,Residential,Wood,1
333743,FL,CLAY COUNTY,0,79520.76,0,0,79520.76,86854.48,0,0,0,0,30.063236,-81.707703,Residential,Wood,3
172534,FL,CLAY COUNTY,0,254281.5,0,254281.5,254281.5,246144.49,0,0,0,0,30.060614,-81.702675,Residential,Wood,1
785275,FL,CLAY COUNTY,0,515035.62,0,0,515035.62,884419.17,0,0,0,0,30.063236,-81.707703,Residential,Masonry,3
995932,FL,CLAY COUNTY,0,19260000,0,0,19260000,20610000,0,0,0,0,30.102226,-81.713882,Commercial,Reinforced Concrete,1
223488,FL,CLAY COUNTY,328500,328500,328500,328500,328500,348374.25,0,16425,0,0,30.102217,-81.707146,Residential,Wood,1
433512,FL,CLAY COUNTY,315000,315000,315000,315000,315000,265821.57,0,15750,0,0,30.118774,-81.704613,Residential,Wood,1
142071,FL,CLAY COUNTY,705600,705600,705600,705600,705600,1010842.56,14112,35280,0,0,30.100628,-81.703751,Residential,Masonry,1
'''

