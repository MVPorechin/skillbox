import math

# start = 'hello world'.capitalize()
# print(f'{start}')
# print(7 + 3)
# print('7 + 3 =', 7 + 3)
# print(1, 2, 3, 4, 5, sep=' + ', end='\n')
# speed = 90
# time = 8
# dist = speed * time
# print(f'{dist}')
# number_one = 11
# number_two = 6
# print(f'{number_one // number_two}')
# print(f'{number_one % number_two}')
# print(f'{number_one ** number_two}')
# print(math.factorial(1000))
# print('Здравствуйте, пожалуйста представитесь')
# username = input('Введите имя: ').title()
# print(f'Привет, {username}!')
# var_a = int(input('Введите значение А: '))
# var_b = int(input('Введите значение В: '))
# print(f'{var_a + var_b}')
# ask_name_phrase = 'Как тебя зовут?'
# print(f'{ask_name_phrase}- спросил я')
# name_phrase = 'Бонд, Джеймс Бонд'
# print(f'Он ответил: {name_phrase}')
# string_a = 10
# int_b = 20
# print(f'{str(string_a)} + {str(int_b)} = {str(string_a + int_b)}')
var_one = 'hello world!'.title()
# print(f'{var_one * 3}')
# print(len(var_one))
# print(var_one[::2])
# print(var_one[::-1])

# print(var_one.find('o'))
# # print(var_one.find('o', 5))
# # print(var_one.rfind('o'))
# # print(var_one.replace('o', '0'))
# # print(var_one.count('o'))

# input_string = input('Введите строку: ')
# input_string = 'in the hole in the ground there liver a hobbit'
# left_letter_h = input_string.find('h')
# right_letter_h = input_string.rfind('h')
# output_sting = input_string[:left_letter_h] + input_string[right_letter_h:]
# print(f"{input_string[:input_string.find('h')] + input_string[input_string.rfind('h'):]}")

# var_two = int(input('Введите число'))
# if var_two >= 0:
#     var_two = - var_two
#     print(f'{var_two}')
# else:
#     print(f'{-var_two}')

# input_int_one = int(input('введите первое число: '))
# input_int_two = int(input('введите второе число: '))
# input_int_three = int(input('введите третье число: '))
#
# if input_int_one > input_int_two and input_int_one > input_int_three:
#     print(f'Максимальное число {input_int_one}')
# elif input_int_two > input_int_one and input_int_two > input_int_three:
#     print(f'Максимальное число {input_int_two}')
# else:
#     print(f'Максимальное число {input_int_three}')

# if (0.1 + 0.2 - 0.3) < 10 ** -13:
#     print('YES')
# else:
#     print('NO')

# float_number = 2.5
# print(int(float_number))
# print(round(-float_number, 3))
# print(math.floor(float_number))

# while
# number_input = int(input('Введите число: '))
# min_number = number_input
# count = 1
# while min_number != 0:
#     number_input = int(input('Введите число: '))
#     if number_input < min_number:
#         min_number = number_input
#
# print(f'{min_number}')

# num = 1
# check_num = True
# while check_num:
#     print(f'{num}')
#     num += 1
#     if num > 100:
#         check_num = False

# number_for_while = 1
# while number_for_while < 100:
#     print(number_for_while)
#     number_for_while += 1
#     if number_for_while > 50:
#         break
# else:
#     print('нормальный выход')

# number_one = -1
# while number_one != 0:
#     number_one = int(input('Введите число: '))
#     if number_one <= 0:
#         continue
#     print(f'{number_one}')

# dist = int(input('Введите растояние: '))

# def sorted_number(num_one, num_two):
#     if num_one < num_two:
#         return num_one, num_two
#     else:
#         return num_two, num_one
#
#
# number_one = int(input('Введите числа: '))
# number_two = int(input('Введите числа: '))
# minimum, maximum = sorted_number(number_one, number_two)
#
# print(f'{minimum, maximum}')


# def is_even(number):
#     return number % 2 == 0
#
#
# num = int(input('Введите число: '))
#
# if is_even(num):
#     print(f'{num} is even')
# else:
#     print(f'{num} is not even')

# def power(a, n):
#     if n == 1:
#         return a
#     return a * power(a, n - 1)
#
#
# int_num = int(input('Введите число: '))
# int_degree = int(input('Введите степень числа: '))
#
# print(f'{int_num} ** {int_degree} = {power(int_degree, int_num)}')

# flavor_list = ['ваниль', 'шоколад', 'пекан', 'земляника']
# for flavor in flavor_list:
#     print( '%s имеет чудесный вкус ' %flavor)

import math
def find_squares(num, squares_amount):
    if squares_amount == 1:
        if math.sqrt(num) == int(math.sqrt(num)):
            return [int(math.sqrt(num))]
        return False
    temporary = 1
    while temporary * temporary < num:
        result = find_squares(num - temporary * temporary, squares_amount - 1)
        if result:
            return [temporary] + result
        temporary += 1
    return False


tries = {0: 1, 1: 1, 2: 2, 3: 3}
number = int(input('Введите число: '))
for index in range(tries[number % 4], 5):
    squares = (find_squares(number, index))
    if squares:
        print(f'Квадрат(ы): {squares} дают в сумме число: {number}')
        break

# def lagrange(n, level):
#     if level == 0:
#         return 0
#     sqrtn = int(n ** 0.5)
#     if sqrtn * sqrtn == n:
#         return str(sqrtn)
#     while sqrtn > 0:
#         if lagrange(n - sqrtn * sqrtn, level - 1) != 0:
#             return str(sqrtn) + " " + lagrange(n - sqrtn * sqrtn, level - 1)
#         sqrtn -= 1
#     return 0
#
#
# n = int(input('Введите число: '))
# print(lagrange(n, 4))


# list_1 = [1, 2, 3, 4]
# list_2 = list_1[:]
# print(f'{list_2}')
#
# dist = {1: 2, 3: 4}
# x = dist.copy()
# x[1] = 5
# print(x, dist)
