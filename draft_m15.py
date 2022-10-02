# print('m15 Задача 1. Таблица степеней')
# numbers = [3, 7, 5]
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for _ in numbers:
#         print(_ ** 2, _ ** 3, _ ** 4)
# print()

# print('m15 Задача 1. Очень простая задача')
# list = []
# for _ in range(100):
#     list.append(_)
# print(list)

# print('m15 Задача 3. Контроль')
# count_personal = int(input('Введите кол-во сотрудников: '))
# list_id = []
# for _ in range(count_personal):
#     id_personal = int(input('ID сотрудника: '))
#     list_id.append(id_personal)
# search_id = int(input('Какой ID ищем?: '))
# if search_id not in list_id:
#     print(f'Сотрудник {search_id} не работает!')
# else:
#     print('Все сотрудники на работе')

# print('m15 Задача 1. Гугл')
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# if nums_list:
#     maximum = nums_list[0]
#     minimum = nums_list[0]
#     for i in nums_list:
#         if maximum < i:
#             maximum = i
#         elif minimum > i:
#             minimum = i
#
# print(f'Максимальное число в списке: {maximum}')
# print(f'Минимальное число в списке: {minimum}')

# print('m15 Задача  2. Кратность')
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for i in range(1, N + 1):
#     num = int(input(f'Введите {i} число: '))
#     nums_list.append(num)
#
# divider = int(input('\nВведите делитель: '))
# index = 0
# sum_indexes = 0
# for number in nums_list:
#     if number % divider == 0:
#         print(f'Индекс числа {number}: {index}')
#         sum_indexes += index
#         index += 1
# print(f'\nСумма индексов: {sum_indexes}\n')
#
# sum_indexes = 0
# for index, number in enumerate(nums_list):
#     if number % divider == 0:
#         print(f'Индекс числа {number}: {index}')
#         sum_indexes += index

# print('m15 Задача 3. Собачьи бега')
# nums_list = []
#
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# if nums_list:
#     maximum = nums_list[0]
#     minimum = nums_list[0]
#
#     minimum_index = 0
#     maximum_index = 0
#     for index, i in enumerate(nums_list):
#
#         if maximum < i:
#             maximum = i
#             maximum_index = index
#
#         if minimum > i:
#             minimum = i
#             minimum_index = index
#
#     print('Максимальное число в списке:', maximum)
#     print('Минимальное число в списке:', minimum)
#
#     print(nums_list)
#     nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
#     print(nums_list)
# else:
#     print('В списке нету чисел')

# word = input('Введите слово: ')
# replace_num = int(input('Номер символа для замены: '))
# replace_sym = input('Чем заменяем: ')
#
# # sym_list = []
# # for sym in word:
# #     sym_list.append(sym)
# sym_list = list(word)
# sym_list[replace_num - 1] = replace_sym
#
# for i in sym_list:
#     print(i, end='')
#
# print(sym_list)

# words_list = []
# counts = [0, 0, 0]
# for i in range(3):
#     print(f'Введите {i + 1} слово: ', end='')
#     word = input()
#     words_list.append(word)
#
# text = input('Слово из текса: ')
# while text != 'end':
#     for index in range(3):
#         if words_list[index] == text:
#             counts[index] += 1
#     text = input('Слово из текса: ')
#
# print('\nПодсчет слов в тексе: ')
# for i in range(3):
#     print(f'{words_list[i]} : {counts[i]}')

print('m15 Задача 3.1. Текстовый редактор: возвращение')
# user_msg = input("Введите строку: ")
user_msg = 'гвозди:шурупы:гайки'
letters = list(user_msg)
what_replace = ':'
for_what_replace = ';'
for index, letter in enumerate(letters):
    if letter == what_replace:
        letters[index] = for_what_replace

for letter in letters:
    print(letter, end='')