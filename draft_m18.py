# user_name = input('Введите имя пользователя: ')
# file_name = input('Введите имя файла: ')
#
# path = 'C:/Users/{mpore}/{AMD_RyzenMaster}.log'.format(
#     mpore=user_name,
#     AMD_RyzenMaster=file_name
# )
#
# path_2 = 'C:/Users/{0}/{0}/{1}.log'.format(
#     user_name,
#     file_name
# )
#
# path_3 = f'C:/Users/{user_name}/{user_name}/{file_name}.log'
#
# print(f'Путь к файлу{path}')

# while True:
#     grats_tamplate = input('Введите шаблон поздравления, '
#                            'в шаблоне необходимо использовать конструкцию {name}: ')
#     if '{name}' in grats_tamplate:
#         break
#     print('Ошибка: отсутствует конструкция {name}')
#
# print('Введите список имен (Заканчивается на end): ')
# names_list = []
# while True:
#     name = input('Имя: ')
#     if name != 'end':
#         names_list.append(name)
#     else:
#         break
#
# for i_name in names_list:
#     print(grats_tamplate.format(name=i_name))

# print('Задача 1. Заказ')
# После того, как человек сделал заказ в интернет-магазине, ему на почту приходит оповещение с его именем и номером заказа.
# Напишите программу, которая получает на вход имя и код заказа, а затем выводит на экран соответствующее сообщение. Для решения используйте строковый метод format.
# name_input = input('Имя: ')
# number_order = input('Номер заказа: ')
# output_text = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(
#     name_input,
#     number_order
# )
# print(output_text)
# print(f'Здравствуйте, {name_input}! Ваш номер заказа: {number_order}. Приятного дня!')

# print('Задача 2. Долги')
# Один наш друг занял у нас определённую сумму денег и всё никак не может их вернуть. А деньги нам нужны. Поэтому мы решили написать небольшой скрипт-напоминалку, который, возможно, разбудит его совесть.
# Напишите программу, которая получает на вход имя и долг, а затем выводит на экран сообщение, где имя повторяется несколько раз (и долг, возможно, тоже). Используйте числа в названиях ключей
# name = input('Введите имя: ')
# debt = input('Введите сумму долга: ')
# text = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!?'.format(name, debt)
# print(text)

# print('Задача 3. IP-адрес')
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой. Каждое число находится в диапазоне от 0 до 255 (включительно).
# Пример правильного адреса: 192.168.1.0
# Пример неправильного адреса: 192.168.300.0
# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес. Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.

# ip_address = "{0}.{1}.{2}.{3}"
# count = 0
# numbers = []
# while count < 4:
#     new_number = int(input("Введите число: "))
#     if 0 <= new_number <= 255:
#         numbers.append(new_number)
#         count += 1
#
# print(ip_address.format(*numbers))
# print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))

# text = input('содержимое файла: ')
# words_list = text.split()
#
# print(words_list)
#
# new_text = '---'.join(words_list)
# print(new_text)

# while True:
#     grats_tamplate = input('Введите шаблон поздравления, '
#                            'в шаблоне необходимо использовать конструкцию '
#                            '{name} и {age}: ')
#     if '{name}' in grats_tamplate and '{age}' in grats_tamplate:
#         break
#     print('Ошибка: отсутствует одна или две конструкции')
#
# names_list = input('Список людей через запятую: ').split(', ')
# ages_str = input('Возраст людей через пробел')
# ages = [int(i_number) for i_number in ages_str.split()]
#
# for i_man in range(len(names_list)):
#     print(grats_tamplate.format(name=names_list[i_man], age=ages[i_man]))
#
# people = [
#     ' '.join([names_list[i_man], str(ages[i_man])])
#     for i_man in range(len(names_list))
# ]
# people_str = ', '.join(people)
# print(f'\n Именинники {people_str}')
