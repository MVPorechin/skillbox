# Задача 1. Работа с файлом
# Реализуйте класс File — контекстный менеджер для работы с файлами. Он должен принимать на вход имя файла и режим
# чтения/записи и открывать сам файл. В начале работы менеджер возвращает файловый объект, а в конце — закрывает файл.
class File:
    def __int__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


# with File('example.txt', 'w') as file:
#     file.write('Всем привет!')


# Задача 2. Пример
#
# На одном собеседовании вам дали такой основной код:
# my_obj = Example()
#
# with my_obj as obj:
#
#     print('Код внутри первого вызова контекст менеджера')
#
#     with my_obj as obj2:
#
#         raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
#
#
#
#     print('Я обязательно выведусь...')
#
#
# Также вместе с этим кодом выдали результат его выполнения:
#
#
#
# Вызов __init__
#
# Вызов __enter__
#
# Код внутри первого вызова контекст менеджера
#
# Вызов __enter__
#
# Вызов __exit__
#
# Тип ошибки: <class 'Exception'>
#
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
#
# "След" ошибки: <traceback object at 0x00000234E54CE4C0>
#
# Вызов __exit__
#
# Тип ошибки: <class 'Exception'>
#
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
#
# "След" ошибки: <traceback object at 0x00000234E54CE4C0>
#
# . . . . (тут сама ошибка красным цветом) . . . .
#
#
#
# Исходя их этих входных данных, реализуйте класс «Контекст-менеджер», который будет выдавать такой же результат.
#
# После этого поправьте класс так, чтобы сработала последняя строчка основного кода. Сам основной код редактировать нельзя.
#
#
#
# Результат с последней строчкой:
#
# Вызов __init__
#
# Вызов __enter__
#
# Код внутри первого вызова контекст-менеджера
#
# Вызов __enter__
#
# Вызов __exit__
#
# Тип ошибки: <class 'Exception'>
#
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
#
# "След" ошибки: <traceback object at 0x00000258ACA4F5C0>
#
# Я обязательно выведусь...
#
# Вызов __exit__

class Example:

    def __init__(self):
        print("Вызов __init__\n")

    def __enter__(self):
        print("Вызов __enter__\n")
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вызов __exit__\n")
        if exc_type:
            print(f'Тип ошибки: {exc_type}\nЗначение ошибки: {exc_val}\n"След" ошибки:{exc_tb}')
        return True  # первый вариант без этой строки, второй с этой строкой


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')
