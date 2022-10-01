# print('15.Задача 1. Таблица степеней')
# numbers = [3,7,5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#
# for _ in number:
#     print(i ** 2, i ** 3, i ** 4)
#     print()

# print('15.Задача 2. Очень простая задача')
# list_number = []
# for _ in range(101):
#     list_number.append(_)
#
# print(list_number)

# print('15.Задача 3. Контроль')
# count_personal = int(input('Кол-во сотрудников в офисе: '))
# list_id = []
# for _ in range(count_personal):
#     id = int(input('ID сотрудника: '))
#     list_id.append(id)
#
# find_id_personal = int(input('Какой ID ищем?: '))
#
# if find_id_personal not in list_id:
#     print('Сотрудник не работает')
# else:
#     print('Сотрудник работает')

# print('15.Задача 2.1. Гугл')
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
# if nums_list:
#     maximum = nums_list[0]
#     minimum = nums_list[0]
#     for i in nums_list:
#         if maximum < i:
#             maximum = i
#         if minimum > i:
#             minimum = i
#
#     print('Максимальное число в списке:', maximum)
#     print('Минимальное число в списке:', minimum)
# else:
#     print('В списке нет чисел')