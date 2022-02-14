def sign_up():
    while True:
        username = input("Введите свой ник: ")
        name = input("Введите свое имя: ")
        surname = input("Введите свою фамилию: ")

        gmail = input("Введите свою почту: ")
        if gmail[-10:] != "@gmail.com":
            print("Почта должна содержать @gmail.com !")
            break
        
        phone = input("Введите номер телефона: ")

        age = 2022 - int(input("Введите год вашего рождения: "))
        if age <= 12:
            print("Сопляк!")
            break
        
        password1 = input("Введите свой пароль: ")
        password2 = input("Повторите свой пароль: ")
        if password1 != password2:
            print("Пиши внимательнее!!!!!!")
            break

        user = dict(
            username=username,
            name=name,
            surname=surname,
            gmail=gmail,
            age=age,
            phone=phone,
            password=password2
        )

        for key, value in user.items():
            print(f"{key}: {value}")
        
        break
    return user

person = sign_up()

def sign_in(user):

    username = input("Введите свой ник: ")
    password = input("Введите пароль: ")

    if username != user['username'] or password != user['password']:
        print("Неверное имя пользователя или пароль!!!")
    else:
        print("Успешная фвторизация <3")

sign_in(person)