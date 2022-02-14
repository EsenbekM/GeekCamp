# Нурзада
# Акбермет 6
# Эрмек
# Жахонгир
# Бекбол  2
# Нурсултан
# Элина 8
# Миртемир

# def sign_up():
    
#     print("__РЕГИСТРАЦИЯ__")

#     username = input("Введите логин: ")
#     name = input("Введите имя: ")
#     surname = input("Введите фамилию: ")

#     while True:
#         gmail = input("Введите почту: ")
#         if gmail[-10:] != '@gmail.com':
#             print("Почта должна содержать @gmail.com!")
#         else:
#             break
    
#     while True:
#         age = 2022 - int(input("Введите год вашего рождения: "))
#         if age < 18:
#             print("Щегол!")
#         else:
#             break
    
#     while True:
#         phone = input("Дай номерочек: ")
#         if phone[:4] != '+996' and len(phone) == 9:
#             phone = '+996' + phone
#             break
#         elif phone[:4] == '+996' and len(phone) == 13:
#             break
#         else:
#             print("Нормально пиши!")


#     while True:
#         password = input("Введите пароль: ")
#         password2 = input("Повторите пароль: ")
#         if password != password2:
#             print("Пароли не совпадают!")
#         else:
#             print("Маладес <3")
#             break

#     user = dict(
#         username=username,
#         name=name,
#         surname=surname, 
#         gmail=gmail,
#         age=age,
#         phone=phone,
#         password=password
#     )

#     print(user)
#     return user


# def sign_in(user: dict):
#     while True:
#         username = input("Введите логин: ")
#         password = input("Введите пароль: ")

#         if username != user['username'] or password != user['password']:
#             print("Неверный логин или пароль!")
#         else:
#             print("ЗАХAДИ)")
#             break
        

# user = sign_up()
# sign_in(user)


name = 'Rus'
surname = 'Mamedov'
print(f'Name: {name}\nSurname: {surname}')