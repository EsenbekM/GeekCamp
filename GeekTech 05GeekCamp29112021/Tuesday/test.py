
def sign_up():
    while True:
        print('__Sign_Up__')
        username = input("Введите свой ник: ")
        name = input("Введите свое имя: ")
        surname = input("Введите свою фамилию: ")

        gmail = input("Введите свой gmail: ")
        if gmail[-10:] != "@gmail.com":
            print("Почта должна содержать @gmail.com !")
            break
        
        phone = input("Введите свой номер: ")

        age = 2021 - int(input("Введите год вашего рождения: "))
        if age < 8:
            print("Щегол иди спи!")
            break

        password1 = input("Введите свой пароль: ")
        password2 = input("Повторите свой пароль: ")
        if password1 != password2:
            print("ЭЭЭ нормально пиши!!!!!")
            break

        user = dict(
            username=username, 
            name=name, 
            surname=surname, 
            gmail=gmail,
            age=age,
            phone=phone,
            password=password1
            )
        
        for key, values in user.items():
            print(f"{key}: {values}")
        break
    return user


person = sign_up()

def sign_in(user):
    username = input("Введите свой ник: ")
    password = input("Введите пароль: ")
    if username != user['username'] or password != user['password']:
        print("Неверный логин или пароль!")
    else:
        print("Успешная авторизация <3 ")

sign_in(person)
