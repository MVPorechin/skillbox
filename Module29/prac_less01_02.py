from contextlib import contextmanager
import time
import os
# Задача 1. Таймер
#
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера:
# функция должна работать с оператором with и замерять время работы вложенного кода.
#
#
#


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(end - start)


with timer() as t:
    val_3 = 300 * 300 ** 3000000

# Задача 2. Директории
#
# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и временно меняет текущую рабочую директорию
# на новую. Функция должна быть контекст-менеджером. Также реализуйте обработку ошибок (например, если такого пути не
# существует). Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться в изначальную рабочую
# директорию. Пример основного кода:
#
# with in_dir('C:\\'):
#
#     print(os.listdir())
#
# Результат:
#
# <тут все папки из вашего диска C>


@contextmanager
def in_dir(path):
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cur_path)


with in_dir('C:\\'):
    print(os.listdir())