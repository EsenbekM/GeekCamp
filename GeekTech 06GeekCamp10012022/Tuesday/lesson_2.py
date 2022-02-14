# LIST

# a = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 'abc', 32.4]

# a.append('Adahan')
# a.insert(3, 'Islam')
# a.remove('abc')
# # a.clear() 
# print(a.count(4))
# a.reverse()
# print(len(a))

# print(a)

# tuple

# names = ('Ivan', 'Alex', 'Egor')
# print(names)


# SET

# names = {'Ivan', 'Alex', 'Egor', 'Ivan', 'Egor'}
# numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
# print(set(numbers))


# DICT

# person = {
#     'name': 'Nurdin',
#     'surname': 'Kubatbekov',
#     'age': 18,
#     'height': 181,
# }

# print(person['age'])
# del person['height']
# a = {'meried': False}
# person.update(dict(meried=False))
# print(person)


# c = 0
# while c < 6:
#     c += 1
#     print(c)

# while True:
#     a = int(input("Введите сумму в сомах: "))

#     if a == 0:
#         break
    
#     print(a * 0.012)

# for i in range(1, 11):
#     print(i)

# s = 'abcdefgu'

# for i in s:
#     print(i)

# number = [1, 2, 4, 5, 6, 7, 8, 9, 9, 34, 54, 5,43,6457,46,34,2]

# chet = []
# nechet = []

# for i in number:
#     if i % 2 == 0:
#         chet.append(i)
#     else:
#         nechet.append(i)

# print(number)
# print(chet)
# print(nechet)

# names = [
#     'Кумарбек', 'Даниел', 'Байел', 'Жениш', 
#     'Инсан', 'Аскар', 'Жаркын', 'Зайнап', 'Эсенбек', 
#     "Нурдинбек", "Тимабек", "Адахан", "Бекболсун",
#     'оолобекаудлацдлцл'
#     ]
# beki = []
# nebeki = []

# for name in names:
#     if 'бек' in name.lower():
#         beki.append(name)
#     else:
#         nebeki.append(name)
# print(names)
# print(beki)
# print(nebeki)

# def say_hello():
#     print('Hello world!')


# say_hello()

# def s(x=2, y=3):
#     return x * y

# abc = s(x=8)
# print(abc)

# names = [
#     'Кумарбек', 'Даниел', 'Байел', 'Жениш', 
#     'Инсан', 'Аскар', 'Жаркын', 'Зайнап', 'Эсенбек', 
#     "Нурдинбек", "Тимабек", "Адахан", "Бекболсун",
#     'оолобекаудлацдлцл'
#     ]
# names2 = ['Esenbek', 'Elina', 'Aibek', 'Aselya', 'Tima', 'Ulanbek', 'Syrgabek', 'Nurperi']

# beki = []
# nebeki = []

# def filter_bek(lst):
#     for name in lst:
#         if 'bek' in name.lower():
#             beki.append(name)
#         else:
#             nebeki.append(name)

# filter_bek(names2)

# print(names2)
# print(beki)
# print(nebeki)

