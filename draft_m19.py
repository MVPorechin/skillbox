# phonebook_dict = {
#     'Ваня': 88006664545,
#     'Петя': 88003332233,
#     'Оля': 89993223322
#                 }
# name = input('Введите имя: ').title()
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#     print('Ошибка: человек с именем {0} не найден'.format(name))



# print('Задача 1. Словарь квадратов чисел')
# На вход программе поступает целое число num. Напишите программу создания словаря, который включает в себя ключи от 1 до num, а значениями соответствующего ключа будет значение ключа в квадрате.
# num = int(input('Введите целое число: ')
# num = 5
# cubes_dict = dict()
# for nums in range(1, num + 1):
#     cubes_dict[nums] = nums ** 2
#
# print(cubes_dict)
#
# print('Задача 2. Студент')
# Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки. Всё вводится в одну строку через пробел. Напишите программу, которая по этой информации составит словарь и выведет его на экран.

# student_str = input(
#     'Введите информацию о студенте через пробел\n'
#     '(имя, фамилия, город, место учебы, оценки): '
#
# )
# student_info = student_str.split()
# student = dict()
# student['Имя'] = student_info[0]
# student['Фамилия'] = student_info[1]
# student['Город'] = student_info[2]
# student['Место учебы'] = student_info[3]
# student['Оценки'] = []
# for index_grade in student_info[4:]:
#     student['Оценки'].append(int(index_grade))
#
# for index_info in student:
#     print(f'{index_info} - {student[index_info]}')


# print('Задача 3. Контакты')
# Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему. И, конечно же, первое, что он захотел в ней реализовать, — это телефонная книга.
# Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона, добавляет их в словарь и выводит на экран текущий словарь контактов. Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.

# phonebook = dict()
# while True:
#     print(f'Текущие контакты на телефоне: ')
#     if phonebook:
#         for name in phonebook:
#             print(f'{name, phonebook[name]}')
#     else:
#         print('<Пусто>')
#     name = input('Введите имя: ')
#     number_phone = int(input('Введите номер телефона: '))
#     if name in phonebook:
#         print('Ошибка: такое имя уже существует.')
#     else:
#         phonebook[name] = number_phone
#

# phonebook_sim_1 = {
#     'Ivan': 100,
#     'Ruban': 200,
#     'Karuban': 300
#
# }
#
# phonebook_sim_2 = {
#     'Uran': 2222,
#     'Buran': 3333,
#     'Ruban': 4444
# }
#
# phonebook_sim_1.update(phonebook_sim_2)
# print(phonebook_sim_1)
#
# phonebook_sim_1['Agrentum'] = phonebook_sim_1.pop('Uran')
# print(phonebook_sim_1)
#
# print(phonebook_sim_1.get('Mulan'))

# print('Задача 1. Склады')
# У мебельного магазина есть два склада, на которых хранятся разные категории товаров по парам «название — количество»:
#
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
# big_storage.update(small_storage)
# search_value = input('Введите товар: ').lower()
# if search_value in big_storage:
#     print(f'Найдено: {search_value} - {big_storage.get(search_value)} штук')
# else:
#     print('Товар не найден')

# print('Задача 2. Кризис фруктов')
# Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре в виде пар «название фрукта — доход»:
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
#
# }
# summ = 0
# min_price = None
# min_name = ''
# for name, value in incomes.items():
#     if min_price is None or min_price > value:
#         min_price = value
#         min_name = name
#     summ += value
#
# incomes.pop(min_name)
# print(f'Общий доход за год составил: {summ}')
# print(f'Самый маленький доход у {min_name}. Он составляет {min_price} рублей')
# print(f'Итоговый словарь: {incomes}')

# def get_value(x):
    # return x[1]


# result_sum = sum(incomes.values())
# min_name, min_value = min(incomes.items(), key=get_value)
# При помощи функции и параметра key мы говорим пайтону как именно надо сравнивать между собой элементы
# Т.к. элементы записаны в таком виде - ('apple': 5600.20), а сравнивать мы хотим по значениям - то нам проосто надо брать для сравнения
# элементы под индексом 1 (если бы сравнивали по ключам, то индекс надо было бы заменить на 0)
# print(result_sum, min_name, min_value)

# print('Задача 3. Гистограмма частоты')
# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться гистограмма частоты букв.
# Напишите программу, которая получает сам текст и считает, сколько раз в строке встречается каждый символ. На экран нужно вывести содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное значение частоты.
#
#
# def histogram(string):
#     sym_dict = dict()
#     for sym in string:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1
#
#     return sym_dict
#
#
# text = input('Введите текст: ').lower()
# hist = histogram(text)
# for index_sym in sorted(hist.keys()):
#     print(f'{index_sym} : {hist[index_sym]}')
#
# print(f'Максимальная частота: {max(hist.values())}')

#
# data = dict()
# print(data.get('server'))
# data['server'] = {
#     'host': '127.0.0.1',
#     'port': '10'
# }
# if data.get('configuration', {}).get('ssh', {}).get('login', {}):
#     print('В структуре уже есть логин')
#
# data['configuration'] = {
#     'ssh': {
#         'access': 'true',
#         'login': 'Ivan',
#         'password': 'qwerty'
#     }
# }
#
# print(data)
# print(data['server']['port'])
# data['configuration']['ssh']['login'] = 'Vladimir'
# print(data['configuration']['ssh']['login'])
# print()
# for index_value in data.values():
#     for index_key in index_value:
#         print(index_key, index_value[index_key])
#
# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
# team_a_members = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'A' and player['status'] == 'Rest'
# ]
# print(team_a_members)

# print('Задача 1. Член семьи')
# Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):
# Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, кол-во лет и дети. Затем, с помощью метода get и установки значения по умолчанию, проверьте есть ли ребёнок с именем Bob. Затем в отдельную переменную получите фамилию этого ребёнка и выведите её на экран. Если у него нет фамилии, то получите значение ‘Nosurname’.
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
#
# childrens_dict = {}
# for child in family_member["children"]:
#     childrens_dict[child["name"]] = child["age"]
#
# search_bob = childrens_dict.get("Bob", None)
# if search_bob:
#     print("Bob найден")
# else:
#     print("Bob-а нету!")
#
# childrens_surname = family_member.get("surname", None)
# if childrens_surname:
#     print(childrens_surname)
# else:
#     print("Nosurname")