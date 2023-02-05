import random
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


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
change_dict(common_dict)
print(common_dict)