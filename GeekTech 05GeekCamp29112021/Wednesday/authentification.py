def sign_up():
    while True:
        username = input("Введите свой ник: ")
        name = input("Введите свое имя: ")
        surname = input("Введите свою фамилию: ")

        gmail = input("Введите свой gmail: ")
        if gmail[-10:] != "@gmail.com":
            print("Почта должна содержать @gmail.com")
            break
        
        phone = input("Введите свой номер: ")

        age = 2021 - int(input("Введите год вашего рождения: "))

        if age < 16:
            print("Доступ запрещен!")
            break

        passw_1 = input("Введите свой пароль: ")
        passw_2 = input("Повторите свой пароль: ")
        if passw_1 != passw_2:
            print("Пароли не совподают!")
            break

        user = dict(
            username=username,
            name=name,
            surname=surname,
            gmail=gmail,
            age=age,
            phone=phone,
            password=passw_2
        )
        print(user)
        break
    return user

person = sign_up()

def login(user):
    username = input("Введите свой ник: ")
    password = input("Введите свой пароль: ")

    if username != user['username'] or password != user['password']:
        print("Неверный логин или пароль!")
    else:
        print("Успешная авторизация)")

login(person)
login(person)
