# 9.1 Модуль os: генерация путей и метод listdir
import os


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

def find_file(cur_path, file_name):
    print(f'переходим: {cur_path}')

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print(f'\t\tсмотрим {path}')
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print(f'{path} это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


file_path = find_file(os.path.abspath(os.path.join('..', '..', 'backup')), 'config.sh')
if file_path:
    print(f'Абсолютный путь к файлу: {file_path}')
else:
    print('Файл не найден')


# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура
# его диска: папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить,
# какой тип иконки вставить. Напишите программу, которая по заданному абсолютному пути определяет, на что указывает
# этот путь (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь
# указывает на файл, то также выведите его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка
# пути на существование.


def find_file(cur_path, file_name):
    print(f'переходим в: {cur_path}')

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        # print(f'\t\tсмотрим в {path}')
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print(f'{path} это директория')
            result = find_file(path, file_name)
            if result:
                break
        if os.path.isfile(path):
            print(f'\tэто {os.path.basename(path)} файл и его размер: {os.path.getsize(path)} байт')
        if os.path.islink(path):
            print(f'\t{path} это ССЫЛКА')
    else:
        result = None

    return result


if os.path.exists(os.path.abspath(os.path.join('..', '..', 'backup'))):
    file_path = find_file(os.path.abspath(os.path.join('..', '..', 'backup')), 'c')
else:
    print('Ошибка, такой папки не существует')

if file_path:
    print(f'Абсолютный путь к файлу: {file_path}')
else:
    print('Файл не найден')
