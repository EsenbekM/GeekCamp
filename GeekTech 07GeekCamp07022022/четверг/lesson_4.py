# Нурзада
# Акбермет
# Эрмек
# Жахонгир
# Бекбол 
# Нурсултан
# Элина - 3
# Миртемир

import random

kmb = ['камень', "ножницы", "бумага"]

while True:

    player = input("Введите камень, ножницы или бумага: ").lower()
    bot = random.choice(kmb)

    if player == 'выход':
        print("Программа завершена!")
        break

    if player == bot:
        print(f"Бот выбрал - {bot}\nВы выбрали - {player}\nНичья!")

    elif (bot == 'камень' and player == 'ножницы') or \
        (bot == "ножницы" and player == "бумага") or \
        (bot == 'бумага' and player == 'камень'):

        print(f"Бот выбрал - {bot}\nВы выбрали - {player}\nБот выиграл!")

    elif (player == 'камень' and bot == 'ножницы') or \
        (player == "ножницы" and bot == "бумага") or \
        (player == 'бумага' and bot == 'камень'):

        print(f"Бот выбрал - {bot}\nВы выбрали - {player}\nВы выиграли!")

import datetime
print(datetime.datetime.now())
