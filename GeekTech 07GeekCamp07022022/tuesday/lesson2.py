# Нурзада
# Акбермет - 5
# Эрмек - 1
# Жахонгир
# Бекбол 
# Нурсултан
# Элина - 8
# Миртемир

# LIST 

# nums = [3, 5, 6, 7, 2, 6, 7, 8, 4, 6, 4, 6, 8, 2, 5]
# names = ['Нурзада', 'Акбермет', 'Эрмек', 'Жахонгир', 'Бекбол' , 'Нурсултан', 'Элина', 'Миртемир']

# names.append('Эсенбек')
# names.insert(2, 'Ислам')
# names.remove('Эрмек')
# del names[-1]
# # names.clear()
# names.reverse()
# print(len(names))

# names.sort()
# nums.sort()
# print(names)
# print(nums)
# print(nums.count(6))

# TUPLE

# names = ('Нурзада', 'Акбермет', 'Эрмек', 'Жахонгир', 'Бекбол' , 'Нурсултан', 'Элина', 'Миртемир')
# print(names)

# # SET

# digits = {2, 4, 6, 7, 4, 2, 5, 7}
# nums = [3, 5, 6, 7, 2, 6, 7, 8, 4, 6, 4, 6, 8, 2, 5]

# l = {'a', 'b', 'c', 'c', 'b', 'a', 'd', 'd'}
# print(l)


# DICT

# person = {
#     'name': 'Ruslan',
#     'age': 18,
#     'city': 'Bishkek',
# }

# person['married'] = False 
# del person['city']
# person.update(dict(height=180))

# print(person)

# # 1) while
# # 2) for

# c = 0
# while True:
#     c += 1
#     print(c)

# while True:
#     num = int(input())

#     if num == 0:
#         break

#     if num % 2 == 0:
#         print("Четное!")
#     else:
#         print("Нечетное!")

# while True:
#     s = int(input("Введите сумму в сомах: "))

#     if s == 0:
#         break

#     print(round(s / 84, 3))


# s = 'abcdef'

# for i in s:
#     print(i)

# nums = [3, 5, 6, 7, 2, 6, 7, 8, 4, 6, 4, 6, 8, 2, 5]
# chet = []
# nechet = []

# for num in nums:
#     if num % 2 == 0:
#         chet.append(num)
#     else:
#         nechet.append(num)

# print(nums)
# print(chet)
# print(nechet)




# def say_hello():
#     print("GeekCamp TOP!")

# say_hello()
# filter_bek()
# filter_bek()
# filter_bek()
# filter_bek()


# def s(x=2, y=2):
#     return x*y

# print(s(3,4))



# names = [
#     'Нурзада', "Нурбек", 'Акбермет', "Бектур", 'Эрмек', 'Жахонгир', 
#     'Бекбол' , 'Нурсултан', "Айбек", 'Элина', 'Миртемир', "Бекзат",
#     'Эсенбек', "Тимабек"
#     ]

# names2 = [
#     'Кумарбек', 'Даниел', 'Байел', 'Жениш', 
#     'Инсан', 'Аскар', 'Жаркын', 'Зайнап', 'Эсенбек', 
#     "Нурдинбек", "Тимабек", "Адахан", "Бекболсун",
#     'оолобекаудлацдлцл'
#     ]

# def filter_bek(x=names):
#     beki = []
#     nebeki = []
#     for name in x:
#         if 'бек' in name.lower():
#             beki.append(name)
#         else:
#             nebeki.append(name)
#     print(beki)
#     print(nebeki)

# filter_bek()