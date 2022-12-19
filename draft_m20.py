import random
import math
import string
# tuple
# Задача 1. Создание кортежей
# Заполните, один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав тем самым третий кортеж. С помощью
# метода кортежа определите в нём количество нулей. Выведите на экран третий кортеж и количество нулей в нём.
first_tuple = tuple(random.randint(0, 5) for number in range(10))
second_tuple = tuple(random.randint(-5, 0) for number in range(10))
triple_tuple = tuple(list(first_tuple + second_tuple))
print(f'Результат: {triple_tuple}, кол-во 0 в кортеже: {triple_tuple.count(0)}')

# Задача 2. Цилиндр
# Андрей однажды уже писал функции для расчёта площади сферы и объёма шара. И теперь для своей
# курсовой работы ему пришлось связаться с цилиндрами. Пользователь вводит два значения: радиус и высоту. Напишите
# функцию для расчёта площади боковой поверхности цилиндра и его полной площади. Функция должна возвращать два эти
# значения. После этого в основной программе выводятся оба ответа в две строки. Площадь боковой поверхности (r —
# радиус, h — высота): Полная площадь (S — площадь круга):


def f_cylinder(radius, heigth):
    side = 2 * math.pi * radius * heigth
    full = side + 2 * (2 * math.pi * radius)
    return side, full


# radius = int(input('Введите радиус: '))
# heigth = int(input('Введите высоту: '))
print(f_cylinder(2, 1))

# Задача 3.  Неправильный код
# Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
# Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный индекс и случайное значение,
# а затем по этим индексу и значению меняет сам кортеж. Функция должна возвращать кортеж и случайное значение. В
# основном коде функция используется два раза, и на экран два раза выводится новый кортеж и случайное значение.
# Причём второй раз выводится сумма первого случайного значения и второго. Однако код, который вам дали,
# оказался нерабочим. Исправьте его в соответствии с описанием.


def change(nums):
    index = random.randint(0, 5) % len(nums)
    value = random.randint(100, 1000)
    nums = list(nums)
    nums[index] = value
    return tuple(nums), value


my_nums = (1, 2, 3, 4, 5)
new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums_second, rand_val_second = change(new_nums)
rand_val += rand_val_second
print(new_nums_second, rand_val)

# Enumarate
# Задача 1. Саботаж! Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам и добавил в
# код сайта символ ~ (тильда). Но программисты быстро решили эту проблему, пройдясь по всему коду маленькой программой.
# Пользователь вводит строку. Напишите программу, которая проходит по строке и выводит в консоль индексы символа ~.
# Для решения этой задачи (и остальных тоже) используйте функцию enumerate.


def sabotage(string):
    result = [index for index, value in enumerate(string) if value == '~']

    return tuple(result)


# text = input('Строка: ')

print(sabotage('so~mec~od~e'))

# Задача 2. Словари из списков
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут
# повторяться). Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
first_list = [random.choice(string.ascii_letters) for letter in range(10)]
second_list = [random.choice(string.ascii_letters) for letter in range(10)]
first_dict = {index: value for index, value in enumerate(first_list)}
second_dict = {index: value for index, value in enumerate(second_list)}
print(f'Первый словарь: {first_dict}\nВторой словарь: {second_dict}')

# Задача 3. Универсальная программа Один заказчик попросил нас написать небольшой скрипт для своих криптографических
# нужд. При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс чётный


def even_value(string):
    list_text = list(string)
    result_list = [value for index, value in enumerate(list_text) if index % 2 == 0]

    return result_list

# text = input('Допустим, есть такая строка: ')

# print(even_value(text))
# print(even_value('О Дивный Новый мир!'))
print(even_value([100, 200, 300, 'буква', 0, 2, 'а']))