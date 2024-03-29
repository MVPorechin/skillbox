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

# Задача 1. Паспортные данные В базе данных поликлиники хранятся паспортные данные людей. Хранение реализовано с
# помощью словаря, состоящего из пар «Серия и номер паспорта — фамилия и имя». Серия и номер — составной ключ,
# а фамилия и имя — составное значение.
# Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека.


def search_in_dict(string):
    string_list = [int(index) for index in string.split()]
    tuple_string = tuple(string_list)
    for key, value in data.items():
        if key == tuple_string:
            return print(f'По запросу: {tuple_string}\nНайдено: {value}')
        else:
            return print(f'По запросу: {tuple_string}\nНичего не найдено')

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

search_value = input('Введите серию и номер через пробел: ')
print(search_in_dict(search_value))

# Задача 2. Контакты 2 Мы уже реализовывали телефонную книгу для Степана, однако её проблема была в том,
# что туда нельзя было добавить людей с одинаковыми именами. Надо это исправить. Напишите программу,
# которая запрашивает у пользователя имя контакта, фамилию и номер телефона, добавляет их в словарь и выводит на
# экран текущий словарь контактов. Словарь состоит из пар «Ф. И. — телефон», где Ф. И. — это составной ключ. Запрос
# на добавление идёт бесконечно (но можно задать своё условие для завершения программы). Обеспечьте контроль ввода:
# если этот человек уже есть в словаре, то выведите соответствующее сообщение.

# phonebook = {}
# while True:
#     text = input('Введите фамилию и имя через пробел:').split()
#     name_surname = tuple(text)
#     if name_surname not in phonebook:
#         phonebook[name_surname] = int(input('Введите номер телефона: '))
#     else:
#         print(f'Контакт {name_surname} уже есть')
#     print(f'{phonebook}')

#zip

names = ['Tom', 'Bob', 'Albert']
ages = [20, 45, 70]
# people = list(zip(names, ages))
people = dict(zip(names, ages))
print(people)
# for index in people:
#     print(index)
people_2 = {index: age + 10 for index, age in zip(names, ages)}
print(people_2)


def input_user_score():
    count_records = int(input('Сколько записей вносится в протокол? '))
    dict_records = dict()
    print('Записи (результат и имя):')
    for number in range(1, count_records + 1):
        user_score = input(f'{number}-ая запись: ').split()
        dict_records[number] = {}
        dict_records[number]['name'] = user_score[1]
        dict_records[number]['score'] = int(user_score[0])
    return dict_records


def result(records):
    winner_rank = dict()
    list_records = [[record.get('score', 0), record.get('name', 0)] for index, record in records.items()]
    max_value = max(list_records)
    winner_rank['First place'] = [max_value[1], max_value[0]]
    for index, values in records.items():
        if max_value[0] > values.get('score') and index < len(records.keys()):
            winner_rank['Second place'] = [values.get('name'), values.get('score')]
    for index, values in records.items():
        if values.get('score') <= winner_rank['Second place'][1] \
                and index < len(records.keys()) \
                and values.get('name') != winner_rank['Second place'][0]:
            winner_rank['Third place'] = [values.get('name'), values.get('score')]
    return winner_rank


def output_winner(list_rank):
    # [print(f'{index, value}') for index, value in list_rank.items()]
    return print(f'{list_rank}')


# dict_records = {
#     1: ('69485', 'Jack'),
#     2: ('95715', 'qwerty'),
#     3: ('95715', 'Alex'),
#     4: ('83647', 'M'),
#     5: ('197128', 'qwerty'),
#     6: ('95715', 'Jack'),
#     7: ('93289', 'Alex'),
#     8: ('95715', 'Alex'),
#     9: ('95715', 'M')
# }


# dict_records = {
#     1: {'name': 'Jack', 'score': 69485},
#     2: {'name': 'qwerty', 'score': 95715},
#     3: {'name': 'Alex', 'score': 95715},
#     4: {'name': 'M', 'score': 83647},
#     5: {'name': 'qwerty', 'score': 197128},
#     6: {'name': 'Jack', 'score': 95715},
#     7: {'name': 'Alex', 'score': 93289},
#     8: {'name': 'Alex', 'score': 95715},
#     9: {'name': 'M', 'score': 95715}
# }


# user_score = input_user_score()
list_winner_rank = result(dict_records)
output_winner(list_winner_rank)