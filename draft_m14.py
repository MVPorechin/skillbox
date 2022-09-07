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

print('m14 Задача  2. Кратность')
nums_list = []
N = int(input('Кол-во чисел в списке: '))

for i in range(1, N + 1):
    num = int(input(f'Введите {i} число: '))
    nums_list.append(num)

divider = int(input('Введите делитель: '))
index = 0
sum_indexes = 0
for number in nums_list:
    if number % divider == 0:
        print(f"Индекс числа {number}: {index}")
        sum_indexes += index
    index += 1

print("Сумма индексов:", sum_indexes)

sum_indexes = 0
for index, number in enumerate(nums_list):  # enumerate в таких случаях очень полезен
    if number % divider == 0:
        print(f"Индекс числа {number}: {index}")
        sum_indexes += index