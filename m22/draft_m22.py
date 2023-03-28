# 9.1 Модуль os: генерация путей и метод listdir
import os
import random

# folder_name = 'project'
# file_name = 'my_file.txt'
# path = 'docs/{folder}/{file}'.format(
#     folder=folder_name,
#     file=file_name,
# )
#
# # print(path)
#
# real_path = os.path.join('docs', folder_name, file_name)
# print(real_path)
# abs_path = os.path.abspath(file_name)
# print(abs_path)
# os.path.abspath('new_folder')
# os.path.abspath(os.path.join('..', 'new_folder'))
# os.path.abspath(os.path.join('/new_folder'))
# os.path.abspath(os.path.join(os.path.sep, 'new_folder'))
#
#
# def print_dirs(project):
#     print(f'\nСодержимое директории {project}')
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print(f'\t\t{path}')
#
#
# projects_list = ['pet_project', 'aqua_disco_project']
#
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join(i_project))
#     print_dirs(path_to_project)
# Задача 1. Сисадмин Вы работаете системным администратором в одной компании. На диске каждого
# сотрудника компании в специальной папке access лежит файл admin.bat. Этот файл предназначен для вас, и вам нужен
# путь до этого файла, причём как относительный, так и абсолютный. Недолго думая, вы решили написать небольшой
# скрипт, который закинете по сети к этому файлу. Напишите программу, которая выводит на экран относительный и
# абсолютный пути до файла admin.bat.
# real_path = os.path.join('access', 'admin.bat')
# abs_path = os.path.abspath(real_path)
# print(f'Абсолютный путь до файла: {abs_path}\nОтносительный путь до файла: {real_path}')

# Задача 2. Содержимое Выберите любую директорию на своём диске и затем напишите программу, выводящую на экран
# абсолютные пути к файлам и папкам, которые находятся внутри этой директории.
# def print_dirs(project):
#     print(f'\nСодержимое директории {project}')
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print(f'\t\t{path}')
#
#
# projects_list = ['pet_project', 'aqua_disco_project']
#
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join(i_project))
#     print_dirs(path_to_project)

# Задача 3. Корень диска Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт.
# Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.
# root_volume = os.path.abspath(os.sep)
# print("Корень диска:", os.path.abspath('.').split("\\")[0])
# print(f'\nКорень диска: {root_volume}')


# def print_dirs(project):
#     print(f'\nСодержимое директории {project}')
#     if os.path.exists(project):
#         for i_elem in os.listdir(project):
#             path = os.path.join(project, i_elem)
#             print(f'\t\t{path}')
#     else:
#         print(f'Каталога проекта {project} не существует')
#
#
# projects_list = ['my_secret_prog', 'pet_project', 'aqua_disco_project']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join(i_project))
#     print_dirs(path_to_project)

# def find_file(cur_path, file_name):
#     print(f'переходим: {cur_path}')
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print(f'\t\tсмотрим {path}')
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             print(f'{path} это директория')
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result


# file_path = find_file(os.path.abspath(os.path.join('../../..', '..', 'backup')), 'config.sh')
# if file_path:
#     print(f'Абсолютный путь к файлу: {file_path}')
# else:
#     print('Файл не найден')
#

# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура
# его диска: папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить,
# какой тип иконки вставить. Напишите программу, которая по заданному абсолютному пути определяет, на что указывает
# этот путь (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь
# указывает на файл, то также выведите его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка
# пути на существование.


# def find_file(cur_path, file_name):
#     print(f'переходим в: {cur_path}')
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         # print(f'\t\tсмотрим в {path}')
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             print(f'{path} это директория')
#             result = find_file(path, file_name)
#             if result:
#                 break
#         if os.path.isfile(path):
#             print(f'\tэто {os.path.basename(path)} файл и его размер: {os.path.getsize(path)} байт')
#         if os.path.islink(path):
#             print(f'\t{path} это ССЫЛКА')
#     else:
#         result = None
#
#     return result
#
#
# if os.path.exists(os.path.abspath(os.path.join('..', '..', 'backup'))):
#     file_path = find_file(os.path.abspath(os.path.join('..', '..', 'backup')), 'c')
# else:
#     print('Ошибка, такой папки не существует')
#
# if file_path:
#     print(f'Абсолютный путь к файлу: {file_path}')
# else:
#     print('Файл не найден')

# path_to = input("Путь: ")
#
# if os.path.isdir(path_to):
#     print("Это папка!")
# elif os.path.isfile(path_to):
#     print("Это файл!")
#     print("Размер файла:", os.path.getsize(path_to), "байт")
# else:
#     print("Указанного пути не существует")

# Задача 2. Поиск файла
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной
# директории. Однако, как мы понимаем, файлов с таким названием может быть несколько. Напишите функцию,
# которая принимает на вход абсолютный путь до директории и имя файла, проходит по всем вложенным файлам и папкам и
# выводит на экран все абсолютные пути с этим именем.


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
# find_file('..', 'test.py')

# list_members_file = open('list_members.txt', 'r', encoding='utf-8')
# input_data = list_members_file.read()
# print(input_data)
# for i_line in list_members_file:
#     print(i_line, end='')
# list_members_file.close()

# Задача 1. Результаты Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей.
# Файл первой группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке
# Additional_info. На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы
# и напоследок — произведение очков уже второй группы. Программист оказался не очень опытным, писал код наобум и даже
# не стал его проверять. И оказалось, этот код просто не работает. Вот что он написал:

# summa, compose, diff = 0, 1, 0
# print(os.listdir())
# file = open(os.path.abspath(os.path.join('task', 'group_1.txt')), 'r', encoding='utf-8')
# file_2 = open(os.path.abspath(os.path.join('task', 'Additional_info', 'group_2.txt')), 'r', encoding='utf-8')
#
# for i_line in file:
#     info = i_line.split()
#     summa += int(info[2])
#     diff -= int(info[2])
#
# for line in file_2:
#     info = line.split()
#     compose *= int(info[2])
#
# file.close()
# file_2.close()
#
# print(f'Сумма: {summa}\nРазность: {diff}\nПроизведение: {compose}')


# Задача 2. Поиск файла 2
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только
# программисту. Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами. Используя
# функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри указанного пути все файлы с
# искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно). Подсказка: можно
# использовать, например, список для сохранения найденного пути.

# def find_file(cur_path, file_name):
#     all_paths = []
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if file_name == i_elem:
#             all_paths.append(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 all_paths.extend(result)
#
#     return all_paths
#
#
# def check_file_inside(path_to_file):
#     file = open(path_to_file, 'r', encoding='utf8')
#     for line in file:
#         print(f'{line}\n')
#     file.close()
#
#
# all_paths = find_file('../pet_project', 'test01.txt')
# check_file_inside(random.choice(all_paths))

# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
#
# counts_file = open('sym_count.txt', 'w')
# counts_file.write(sym_count_str)
# counts_file.write(str(50))
# counts_file.close()


# def find_file(cur_path, file_name):
#     print(f'переходим: {cur_path}')
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print(f'\t\tсмотрим {path}')
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             print(f'{path} это директория')
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# # file_path = find_file(os.path.abspath(os.path.join('../../..', '..', 'backup')), 'config.sh')
# file_path = find_file(os.path.abspath(os.path.join('../../..', '..', 'documents')), 'squid.conf')
# hystory_file = open('search_hystory.txt', 'a')
#
# if file_path:
#     print(f'Абсолютный путь к файлу: {file_path}')
#     hystory_file.write(f'{file_path} \n')
# else:
#     print('Файл не найден')
# hystory_file.close()

# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите
# программу, которая выводит их сумму в выходной файл answer.txt.
# numbers_file = open('numbers.txt', 'r')
# summary_file = open('anwswer.txt', 'a')
# summ = 0
# for value in numbers_file:
#     summ += int(value)
# summary_file.write(str(summ))
# numbers_file.close()
# summary_file.close()

# Задача 2. Всё в одном
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город,
# и там у него случилась беда: его диск пришлось отформатировать, а доступ в интернет отсутствует. Остался только
# телефон с мобильным интернетом. Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом
# все решения и скрипты, которые у вас сейчас есть. Напишите программу, которая копирует код каждого скрипта в папке
# проекта python_basic в файл scripts.txt, разделяя код строкой из 40 символов *.

# def find_file(cur_path, ending):
#     all_paths = []
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if i_elem.endswith(ending):
#             all_paths.append(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, ending)
#             if result:
#                 all_paths.extend(result)
#
#     return all_paths
#
#
# def get_text_from_file(path_to_file):
#     file = open(path_to_file, "r", encoding="utf8")
#     result = ""
#     for line in file:
#         result += line
#     return result
#
#
# all_py_files = find_file(os.path.abspath(os.path.join('..', '..', 'skillbox')), '.py')
#
# file_result = open("scripts.txt", "w", encoding="utf8")
#
# for file_path in all_py_files:
#     file_result.write(get_text_from_file(file_path))
#     file_result.write("\n" * 2 + "*" * 80 + "\n" * 2)


speakers_file = open('speakers.txt', 'r', encoding='utf-8')
data = speakers_file.read(14)
speakers_file.seek(0)
data_2 = speakers_file.read(22)
print(data)
print(data_2)
speakers_file.close()