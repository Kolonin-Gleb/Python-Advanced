# Основы работы со словорями
'''
Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке),
у которых нет информации об электронной почте. 
Примечание 1. Ключ email может отсутствовать в словаре.

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

no_email_users = []

for user in users:
    if not 'email' in user.keys() or user['email'] == '':
        no_email_users.append(user['name'])

print(*sorted(no_email_users))

'''
# Строковое представление
'''
digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}

num = input()

for dig in num:
    print(digits[int(dig)], end=' ')
'''
# Информация о курсе
'''
# Словарь courses
# Ключи словаря - номера курсов. Их значения - словари с информацией о них
courses = {
    'CS101': [3004, 'Хайнс', '8:00'],
    'CS102': [4501, 'Альварадо', '9:00'],
    'CS103': [6755, 'Рич', '10:00'],
    'NT110': [1244, 'Берк', '11:00'],
    'CM241': [1411, 'Ли', '13:00']
}

course_num = input()

print("course_num: ", end='')
print(*courses[course_num], sep=', ')
'''
# Набор сообщений
'''
msg = input().capitalize()

encoder = {}
'''

# Аннаграммы 1
'''
# Посчитать кол. всех букв в 1 вводе
# Посчитать кол. всех букв в 2 вводе
# Если все ключи совпадают и соответствующие им значения тоже, то Аннаграммы
lst1 = [el for el in input()]
lst2 = [el for el in input()]

res1 = {}
res2 = {}

for el in lst1:
    res1[el] = res1.get(el, 0) + 1
for el in lst2:
    res2[el] = res2.get(el, 0) + 1

if res1 == res2:
    print("YES")
else:
    print("NO")
# Более элегантное решение
print(("NO", "YES")[sorted(input()) == sorted(input())])
'''

'''
p = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~: "
str1 = [el for el in input().lower() if el not in p]
str2 = [el for el in input().lower() if el not in p]

print(("NO", "YES")[sorted(str1) == sorted(str2)])
# Вижу зверей
# Живу резвей
'''

# Телефонная книга
# Разница в работе setdefault и get
# 1) book.setdefault(name, []).append(mobile)
# 2) book[name] = book.get(name, []).append(mobile) # НЕПРАВИЛЬНО
# 2) book[name] = book.get(name, []) + [mobile] # ПРАВИЛЬНО
'''
contacts = dict()

friends = int(input())
for i in range(friends):
    phone, name = input().split(" ")
    # Сохранение контактов
    contacts[name] = contacts.get(name, []) + [phone]

names = []
requests = int(input())
for i in range(requests):
    names.append(input().capitalize())


# output
for i in range(requests):
    name = names.pop(0)
    if name not in contacts.keys():
        print('абонент не найден')
    else:
        print(*contacts.get(name), sep=' ')
'''

