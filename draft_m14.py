# print('m14 Задача 1. Таблица степеней')
# numbers = [3, 7, 5]
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for _ in numbers:
#         print(_ ** 2, _ ** 3, _ ** 4)
# print()

# print('m14 Задача 1. Очень простая задача')
# list = []
# for _ in range(0,101):
#     list.append(_)
# print(list)

# print('m14 Задача 3. Контроль')
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

# print('m14 Задача 1. Гугл')
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

# print('m14 Задача  2. Кратность')
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

print('m14 Задача 3. Собачьи бега')
nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

if nums_list:
    maximum = nums_list[0]
    minimum = nums_list[0]

    minimum_index = 0
    maximum_index = 0
    for index, i in enumerate(nums_list):

        if maximum < i:
            maximum = i
            maximum_index = index

        if minimum > i:
            minimum = i
            minimum_index = index

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)

    print(nums_list)
    nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
    print(nums_list)
else:
    print('В списке нету чисел')