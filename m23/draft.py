import os


# def divide(number):
#     return 10 / number
#
#
# def sum_of_diveded(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError as exc:
#             print(f'{exc, type(exc)} - на ноль делить нельзя')
#     return div_sum
#
#
# total = 0
# try:
#     number_file = open('numbers.txt', 'r')
#     for i_line in number_file:
#         nums_list = i_line.split()
#         first_num = int(nums_list[0])
#         second_num = int(nums_list[1])
#
#         total += sum_of_diveded(first_num, second_num)
#     print(f'Общая сумма {total}')
#
# except ZeroDivisionError as exc:
#     print(f'{exc, type(exc)} - на ноль делить нельзя')
# except FileNotFoundError as exc:
#     print(f'{exc, type(exc)} - Такого файла или каталога нет')
#
# answer_file = open('answer.txt', 'w')
# try:
#     answer_file.write(f'The answer is: {str(total)}')
# except TypeError as exc:
#     print(f'{type(exc), exc}')
# else:
#     print('Программа выполнилась без ошибок')
# finally:
#     answer_file.close()
#     print(answer_file.closed)

# Задача 1. Пятый элемент
# В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый элемент строки,
# введённой пользователем. Вот код студента:

# BRUCE_WILLIS = 42
# input_data = input('Введите строку: ')
#
# try:
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#     print(f'Leeloo Dallas! Multi-pass № {result}!')
# except ValueError as exc:  # as - этот оператор запишет пойманное исключение в переменную exc (название может быть
#     # любым)
#     print(f'{exc, type(exc)} — невозможно преобразовать к числу')
# except IndexError as exc:
#     print(f'{exc, type(exc)} — выход за границы списка')
# except Exception as exc:
#     print(f'{exc, type(exc)} - "поймано исключение')


#Задача 2. Возраст

# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека. Напишите программу,
# которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита) и выводит
# результат в новый файл result.txt в формате «имя — возраст». Программа должна обрабатывать следующие ошибки и
# выводить сообщение на экран: Попытка создания файла, который уже существует. На чтение ожидался файл,
# но это оказалась директория. Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково). При
# желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

# file_ages = None
# file_result = None
#
# try:
#     file_ages = open("ages.txt", "r", encoding="utf8")
#     file_result = open("result.txt", "x", encoding="utf8")
#     # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
# except (FileExistsError, PermissionError) as exc:  # названия исключений можно группировать в кортежи
#     print(f'{exc, type(exc)} - Поймано исключение ')
# except FileNotFoundError as exc:
#     print(f'{exc, type(exc)} - Файл не найден ')
#
# if file_result and file_ages:
#     names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     count = 0
#     for line in file_ages:
#         try:
#             clear_line = line.rstrip()
#             int(clear_line)  # на всякий случай пытаемся преобразить данные в int, но не сохраняем это в переменную, т.к. записывать нам
#             # в файл придётся именно строку
#             file_result.write(names[count] + ' - ' + clear_line + '\n')
#             count += 1
#         except (ValueError, TypeError) as exc:
#             print(f'{exc, type(exc)} - Поймано исключение ')


# Задача 1. Простая программа Напишите программу, которая открывает файл и записывает туда введённую пользователем
# строку. Используйте операторы try except else finally. Обработайте возможные ошибки: Проблема при открытии файла.
# Нельзя преобразовать данные в целое. Неожиданная ошибка.

# file = None
# try:
#     file = open("23.3.txt", "w", encoding="utf8")
#     number = int(input("Введите текст: "))
#     file.write(str(number))
# except (FileNotFoundError, PermissionError) as exc:
#     print(type(exc), exc)
# except ValueError as exc:
#     print(type(exc), exc)
# except Exception as exc:
#     print(type(exc), exc)
# else:
#     print("Запись прошла без ошибок")
# finally:
#     if file and not file.closed:
#         file.close()


# Задача 2. Старая задача
#
# Возьмите любую задачу из практической работы, например, предыдущего модуля и оформите её решение
# в виде try except finally (можно ещё и else), обрабатывая возможные ошибки.
#
# Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос:
# когда стоит использовать обработку исключений и когда она будет излишней?


# def find_file(cur_path, file_name):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if file_name == i_elem:
#             print(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# try:
#     find_file('c:\\', 'hel')
# except (TypeError, PermissionError) as exc:
#     print(exc, type(exc))

# Хоть проверка исключений и является мощным инструментом, НО отдавать предпочтение нужно простым проверкам (избежать исключения лучше)
# Если же мы не уверены в появлении ошибки (например у нас нет власти над источником ошибки - это может быть какой-то сторонний сервис)
# И если простая проверка не поможет учесть все варианты - мы можем использовать исключения.
# НО даже в этом случае, старайтесь разделять исключения, которые вы выбрасываете специально и исключения которые могут появиться случайно.
# Причина такой осторожности в том, что мы можем запутаться и поймать например исключение, о котором мы не догадывались. А если мы его
# поймаем и не увидим - мы можем пропустить ошибку в нашем коде.

# line_count = 0
# sym_sum = 0
# try:
#     people_file = open('people.txt', 'r')
#     for i_line in people_file:
#         length = len(i_line)
#         line_count += 1
#         if i_line.endswith('\n'):
#             length -= 1
#         if length < 3:
#             raise BaseException(f'Длинна {line_count} строки меньше трех символов')
#         sym_sum += length
#     people_file.close()
#
#
# except FileNotFoundError as exc:
#     print(f'{type(exc), exc} - Файл не найден')
#
# finally:
#     print(f'Найденная сумма символов: {sym_sum}')

names_list = []
while True:
    try:
        name = input('Введите имя: ')
        if not name.isalpha():
            names_list.append(name)
        if len(names_list) == 5:
            print('Место закончилось')
            break
    except TypeError:
        print(f'Ты чего ввел? {name}')


names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('программа закончена, запись завершена')