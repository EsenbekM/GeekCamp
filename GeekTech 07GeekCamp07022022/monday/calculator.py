# Напишите простой калькулятор, который считывает с 
# пользовательского ввода три строки: первое число,
#  второе число и операцию, после чего применяет операцию
#  к введённым числам ("первое число" "операция" "второе число")
#  и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, 
# необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят 
# вещественные числа.


x = float(input("Введите первое число: "))
oper = input("Введите операцию(+, -, *, /, pow, mod, div):")
y = float(input("Введите второе число: "))

if oper == '+':
    print(x+y)

elif oper == '-':
    print(x-y)

elif oper == '*':
    print(x*y)

elif oper == 'pow':
    print(x**y)

elif oper == '/':
    print(x/y)

elif oper == 'mod':
    print(x%y)

elif oper == 'div':
    
    print(x//y)

else:
    print("Такой операции нет!")