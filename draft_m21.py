import random
import copy
## home work
# def shortest_seq_range(string, tpl):
#     return min(len(string), len(tpl))
#
#
# syms_str = 'abcd'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = ((syms_str[i_elem], nums_tpl[i_elem]) for i_elem in range(shortest_seq_range(syms_str, nums_tpl)))
# print(f'{pairs}')
# def factorial(num):
#     if num == 1:
#         return 1
#     fact_m_minus_1 = factorial(num - 1)
#     return num * fact_m_minus_1
#
#
# num_fuct = factorial(5)
# print(num_fuct)
#
#
# def fibonacci(n):
#     """ Returns Fibonacci Number at nth position using recursion"""
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(10):
#     print(fibonacci(i), end=" ")

# Источник: https://pythononline.ru/osnovy/rekursii-python

# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой то блок',
#             'p': 'А вот тут новый абзац'
#         }
#     }
# }
#
#
# def find_key(struct, key):
#     if key in struct:
#         return struct[key]
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# user_key = input('Какой ключ ищем?: ')
# value = find_key(site, user_key)
# if value:
#     print(value)
# else:
#     print('Такого ключа в структуре сайта нет')

# Задача 1. Challenge Обычно программисты любят, когда всё просто и понятно. Но Антон не из таких. Он любит
# устраивать себе челлендж, развиваться и сразу применять на практике то, что только что узнал. И в этот раз он
# подумал реализовать подсчёт факториала без использования циклов. Напишите функцию, которая считает факториал числа
# с помощью рекурсии. Кстати, в Python есть ограничение на количество рекурсивных вызовов. Попробуйте передать своей
# функции, например, число 1000 и посмотрите, что будет.

# def factorial(num):
#     if num == 1:
#         return 1
#     fact_m_minus_1 = factorial(num - 1)
#     return num * fact_m_minus_1
#
#
# num_fuct = factorial(995)
# print(num_fuct)


# Задача 2. Степень числа На одном из форумов, посвящённых программированию, пользователь выложил такой код для
# расчёта степени числа без использования циклов, ** и функции math.pow(): Другие пользователи отметили,
# что это решение нерабочее и в нём есть ошибки. Исправьте это решение, не используя циклы, возведение в степень
# через ** и функцию math.pow()
# Правильный результат:
# Введите вещественное число: 1.5
# Введите степень числа: 5
# 1.5 ** 5 = 7.59375


# def power(a, n):
#     if n == 1:
#         return a
#     else:
#         return a * power(a, n - 1)
#
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
#
# print(f'{float_num} ** {int_num} = {power(float_num, int_num)}')


# Задача 3. Поиск элемента Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по
# ней и найти нужный элемент. Для этого в программировании используются специальные алгоритмы поиска.
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран. В
# качестве примера можно использовать такой словарь:


# def search_element(data, tag):
#     result = None
#     if tag in data:
#         return data[tag]
#     for key, value in data.items():
#         if isinstance(value, dict):
#             result = search_element(value, tag)
#             if result:
#                 return result
#     return result

#
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт "TITLE"'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок "H2"',
#             'div': 'Тут, наверное, какой то блок "DIV"',
#             'p': 'А вот тут новый абзац "P"'
#         }
#     }
# }
#
#
# search_key = input('Введите искомое значение: ')
# return_value = search_element(site, search_key)
# if return_value:
#     print(f'Найдено значение: {return_value}')
# else:
#     print(f'Значение подходящих с {search_key} не найдено.')
# def foo(x):
#     if x == 0:
#         print("Вызов foo(0) возвращает 0")
#         return 0
#     else:
#         print(f"Вызов foo({x - 1}) начинается и добавляется в стек")
#         new_result = foo(x - 1)
#         print(f"Вызов foo({x - 1}) завершился и удаляется из стека")
#         result = x + new_result
#         return result
#
#
# print(f"Вызов foo(2) начинается и добавляется в стек")
# result = foo(2)
# print(f"Вызов foo(2) завершается и удаляется из стека")
# print("Итоговый ответ — ", result)


# def sum_test(x, y):
#     return x + y
#
#
# def test_return(a, b, c):
#     new_summ = sum_test(a, b)
#     # — вызывая эту функцию, мы хотим получить промежуточный результат; мы не хотим, чтобы наша функция завершилась;
#     result = new_summ + c
#     # получив результат вложенной функции, мы его изменяем
#     # и возвращаем
#     return result
#
#
# value = test_return(1, 2, 3)

# def try_to_change_values(some_list, num):
#     for i_index, i_val in enumerate(some_list):
#         some_list[i_index] += 10
#
#
# my_list = [1, 2, 3]
# number = 100
# try_to_change_values(my_list, number)
# print(f'{my_list, number}')

# Задача 1. Ошибка В одном проекте на 10 000 строк кода произошла критическая ошибка. Хорошо, что старший разработчик
# быстро её нашёл и исправил. Он решил проверить, смогли бы вы её исправить, если бы его не было на месте. Поэтому он
# написал для вас код с аналогичной ошибкой:

# Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых равны ранее объявленным
# переменным. Затем вызывается функция, которая должна изменять значения словаря, добавляя к значениям случайное
# число, в зависимости от типа данных. Но при этом меняются и ранее объявленные переменные. Исправьте эту ошибку и
# убедитесь, что nums_list, some_dict и uniq_nums не меняются.


# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# # common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
# common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
# # common_dict_2 = copy.deepcopy(common_dict)
# # Она будет особенно полезна в структурах, в которых множество вложенных переменных
# change_dict(common_dict)
# print(common_dict)

# Задача 2. Непонятно! Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками,
# объектами и их id. Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных, информацию о
# его изменяемости, а также id этого объекта.


# def check_value(val):
#     if isinstance(input_data, str):
#         print(f'Тип данных: str (строка)\nНеизменяемый (immutable)\nId обьекта: {id(input_data)}')
#     if isinstance(input_data, int):
#         print(f'Тип данных: int (целое число)\nНеизменяемый (immutable)\nId обьекта: {id(input_data)}')
#     if isinstance(input_data, float):
#         print(f'Тип данных: float (числа с плавающей точкой)\nНеизменяемый (immutable)\nId обьекта: {id(input_data)}')
#     if isinstance(input_data, tuple):
#         print(f'Тип данных: tuple (кортеж)\nНеизменяемый (immutable)\nId обьекта: {id(input_data)}')
#     if isinstance(input_data, bool):
#         print(f'Тип данных: bool (булево значение)\nНеизменяемый (immutable)\nId обьекта: {id(input_data)}')
#     if isinstance(input_data, list):
#         print(f'Тип данных: list (список)\nИзменяемый(mutable)\nId обьекта: {id(input_data)}')
#     if isinstance(input_data, dict):
#         print(f'Тип данных: dict (словарь)\nИзменяемый(mutable)\nId обьекта: {id(input_data)}')
#     if isinstance(input_data, set):
#         print(f'Тип данных: set (множество)\nИзменяемый(mutable)\nId обьекта: {id(input_data)}')
#
#
# input_data = input('Введите данные: ')
# check_value(input_data)


# Ввод объекта осуществляется не через инпут (решение с инпутом можно реализовать, но для этого придётся прописывать
# множество проверок введенной строки, чтобы можно было преобразовать её потом в нужный тип данных)

# Добавим вспомогательные словари для работы (в них можно будет по необходимости добавлять типы, которых сейчас нет)
# data_names_dict = {
#     "<class 'str'>": "строка",
#     "<class 'dict'>": "словарь",
#     "<class 'list'>": "список",
#     "<class 'set'>": "множество"
# }
#
# mutable_check_helper = {
#     "mutable": ("словарь", "список", "множество")
# }
#
# def check_info(data):
#     type_of_data = type(data)
#     name_of_data = ""
#     if str(type_of_data) in data_names_dict:
#         name_of_data = data_names_dict[str(type_of_data)]
#
#     if name_of_data in mutable_check_helper["mutable"]:
#         property_of_data = "Изменяемый (mutable)"
#     else:
#         property_of_data = "Неизменяемый (immutable)"
#
#     print(f"Тип данных: {type_of_data} ({name_of_data})")
#     print(property_of_data)
#     print("Id объекта:", id(data))
#
#
# data_in = "привет"
# check_info(data_in)
# check_class = ['123', 123]
# print(type(check_class), isinstance(check_class, list))

# def ask_user(question,
#              complaint='Неверный ввод. Пожалуйста, введите да или нет',
#              retries=4):
#     while True:
#         answer = input(question).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint)
#         print(f'Осталось попыток: {retries}')
#
#
# ask_user('Вы действительно хотите выйти? ')
# ask_user('Удалить файл?', 'Так удалить или нет?')
# ask_user('Записать файл? ', retries=2)

# Задача 1. Работа с файлом Вы пишете небольшое приложение для работы с файлами. Реализуйте функцию, которая может
# принимать на вход три аргумента: вопрос пользователю (на который нужно ответить да или нет), сообщение о
# неправильном вводе и количество попыток. Вопрос — обязательный позиционный аргумент, остальные — со значениями по
# умолчанию. При корректном ответе функция может возвращать что угодно — например, число 1 при ответе «да» или 0 при
# ответе «нет». В основной программе вызовите функцию минимум три раза: только с вопросом, с вопросом и сообщением об
# ошибке, с вопросом и количеством попыток.

# def work_at_file(question,
#                  complaint="Неверный ввод. Пожалуйста введите 'да' или 'нет'.",
#                  retries=4):
#     retry = True
#     while retry:
#         answer = input(question).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             retry = False
#         print(complaint)
#         print(f'Осталось попыток: {retries}')
#
#
# work_at_file('Вы действительно хотите выйти? ')
# work_at_file('Удалить файл? ', 'Так удалить или нет? ')
# work_at_file('Записать файл? ', retries=2)

# Задача 2. Накопление значений При работе со значениями по умолчанию и изменяемыми типами данных нужно знать и
# остерегаться ещё одной интересной штуки.
# Напишите функцию с двумя аргументами: первый — число num, позиционный аргумент; второй — список lst, по умолчанию
# он пустой. В теле функции в список добавляется число num и сам список выводится на экран.
# В основной программе вызовите функции три раза только с одним аргументом (числом), например так:


# def add_num(num,
#             lst=[]):
#     lst.append(num)
#     print(f'{lst}')

# И посмотрите, что произойдёт.
# После этого сделайте значение lst по умолчанию None и поправьте функцию, чтобы она работала правильно.

# def add_num(num,
#             lst=None):
#     lst = lst or []
#     # if not lst:
#     #     lst = []
#     lst.append(num)
#     print(f'{lst}')
#
#
# add_num(5)
# add_num(10)
# add_num(15)

# Задача 3. Помощь другу Нашего друга попросили написать функцию, которая на вход принимает список всякого мусора.
# Ему нужно подготовить из этого списка список словарей, чтобы его коллеги смогли дальше продолжить обработку данных.
# Вот список правил, что нужно сделать с изначальным списком: Если в списке встретился словарь, то оставляем его.
# Если в списке встретилась строка, то из неё нужно сделать словарь и положить его в итоговый список, например  “abc”
# → {“abc”: “abc”}. С числами нужно сделать то же самое, что и со строками. Всё остальное выкидываем из нашего списка.
# Друг написал программу, но в ней ошибка, так как она что-то не то выводит:( Нужна ваша помощь, вот сама программа:


# def create_dict(data, template=dict()):
#     if isinstance(data, dict):
#         return data
#     elif isinstance(data, (int, str, float)):
#         template = template or dict()
#         template[data] = data
#         return template
#     else:
#         return None
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         new_elem = create_dict(i_element)
#         if new_elem:
#             new_list.append(new_elem)
#     return new_list
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)


def print_tax_document(tax, *args, **kwargs):
    price_summ = 0
    price_summ = [price_summ + i_price * tax / 100 for i_price in args]
    print(f'Сумма цен с учетом налога: {sum(price_summ)}')

    for i_info, i_value in kwargs.items():
        print('{}: {}'.format(i_info, i_value))


my_tax = int(input('Величина налога: '))
print_tax_document(my_tax, 1000, 950, 880, 920, 990,
                   year=1997, doc_type='report', operation_id=1110034)