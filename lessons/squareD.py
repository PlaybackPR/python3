user_name = input('Input your name: ')
print('Hello ' + str(user_name) + ' !')
user_pass = input('Generete your password: ')
rew_pass = input('Потвердите ввод пароля еще раз: ')
while user_pass != rew_pass:
    rew_pass = input('Пароли не совпадают, введите еще раз: ')
    if user_pass == rew_pass:
        break
print('Ваш пароль принят')
