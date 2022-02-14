a = 23            # int
b = 10.4          # float
s = "29"          # str
t = True          # bool
 
# name = 'Nurik'
# surname = 'KKKKK'
# age = 18

# print("Имя", name)
# print('Возраст', age)

# print(s)

# age = int(input("Введите год рождения: "))
# print(2021 - age)

# +, -, *, /, x**y, //, % 

# x = 10
# y = 3
# s = x % y
# print(s)

# # ==, !=, <, >, <= >=
# a = 6
# b = 2
# print(a > b)



# s = 'abcdefg'
# print(s[2:5])

# name = 'esenbek'
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.count('e'))

# a = int(input())
# b = int(input())
# s = a+b

# print(f"Сумма равна {s}")

password = '1234'
a = input("Введите пароль: ")

if a == password:
    print("Добро пожаловать!")
else:
    print("Доступ запрещен!")

svet = input("Введите цвет: ")
if svet == 'green':
    print('go')
if svet == 'yellow':
    print('ready')
if svet == 'red':
    print('stop')


# n = int(input())

# if n % 2 == 0:
#     print(f"{n} - четное")
# else:
#     print(f"{n} - нечетное")





# Напишите простой калькулятор, который считывает с пользовательского ввода
#  три строки: первое число,
#  второе число и операцию, после чего применяет операцию к введённым числам
#  ("первое число" "операция" "второе число")
#  и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить
#  строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.


x = float(input("Введите первое число: "))
oper = input("Введите операцию(+, -, *, /, pow, mod, div): ")
y = float(input("Введите второе число: "))

if oper == "+":
    result = x + y

elif oper == "-":
    result = x - y

elif oper == "*":
    result = x * y

elif oper == "pow":
    result = x ** y

elif oper == "mod":
    result = x % y

elif oper == "/":
    result = x / y

elif oper == "div":
    result = x // y

else:
    print("Такой операции нет!")

print(f"Ответ - {result}")