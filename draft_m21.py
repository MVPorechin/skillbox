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

def power(a, n):
    return a * power(a, n)


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))

# Правильный результат:
# Введите вещественное число: 1.5
# Введите степень числа: 5
# 1.5 ** 5 = 7.59375


# Задача 3. Поиск элемента Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по
# ней и найти нужный элемент. Для этого в программировании используются специальные алгоритмы поиска.
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран. В
# качестве примера можно использовать такой словарь:

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