def sign_up():
    while True:
        print("__Sign Up__")
        username = input("Please enter your username: ")
        name = input("Please enter your name: ").capitalize()
        surname = input("Please enter your surname: ").capitalize()
 
        gmail = input("Please enter your gmail: ")
        if gmail[-10:] != "@gmail.com":
            print("Почта должна содержать @gmail.com !")
            break

        age = 2021 - int(input("Please enter date of your birthd: "))
        if age < 8:
            print("Acces deniet!")
            break

        pass1 = input("Please enter your password: ")
        pass2 = input("Please repeat your password: ")
        if pass1 != pass2:
            print("Enter password correctly!")
            break

        user = dict(username=username, name=name, surname=surname, gmail=gmail, age=age, password = pass1)


        print("\n__Your profile__")
        for key, value in user.items():
            print(f"{key}: {value}")
        break
    return user

def sign_in(dct):
    print("\n__Sign in__")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != dct["username"] or password != dct["password"]:
        print("Incorrect password or username!")
    else:
        print("\nYou are signed in <3")

user = sign_up()
sign_in(user)