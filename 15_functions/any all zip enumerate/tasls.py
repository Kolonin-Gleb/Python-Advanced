# step 11 correct ip

# Напишите программу с использованием встроенной функции all()

print(all(x.isdigit() and int(x) < 256 for x in input().split('.')))

# user_adress = input().split('.')
# user_adress = list(map(lambda part: part if part.isdigit() else '999', user_adress))
# user = list(map(lambda part: True if (int(part) <= 255) else False, user_adress))
# print(all(user))
