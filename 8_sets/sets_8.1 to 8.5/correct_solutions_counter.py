# Step 15 Счётчик верных решений
"""
"""
answers = int(input()) # Кол. ответов
users = set() # Пользователи
correct_answers = 0 # Кол. верных ответов
users_completed = set() # Уникальные пользователи ответившие верно

for i in range(answers):
    user, result = input().split(": ")
    users.add(user) # Всегда пробуем добавить нового пользователя

    if user not in users_completed and result == 'Correct':
        users_completed.add(user)
        correct_answers += 1
    elif result == 'Correct':
        correct_answers += 1
    

if correct_answers == 0:
    print('Вы можете стать первым, кто решит эту задачу')
else:
    successful_attempts_percentage = int((correct_answers * 100 / answers) + 0.5)
    print(f'Верно решили {len(users_completed)} учащихся')
    print(f'Из всех попыток {successful_attempts_percentage}% верных')




