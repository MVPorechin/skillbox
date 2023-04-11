def divide(number):
    return 10 / number


def sum_of_diveded(left, right):
    div_sum = 0
    for i_num in range(left, right + 1):
        try:
            div_sum += divide(i_num)
            print(div_sum)
        except ZeroDivisionError as exc:
            print(f'{exc, type(exc)} - на ноль делить нельзя')
    return div_sum


total = 0
try:
    number_file = open('numbers.txt', 'r')
    for i_line in number_file:
        nums_list = i_line.split()
        first_num = int(nums_list[0])
        second_num = int(nums_list[1])

        total += sum_of_diveded(first_num, second_num)
    print(f'Общая сумма {total}')

except ZeroDivisionError as exc:
    print(f'{exc, type(exc)} - на ноль делить нельзя')
except FileNotFoundError as exc:
    print(f'{exc, type(exc)} - Такого файла или каталога нет')

#Задача 1. Пятый элемент

# В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый элемент строки,
# введённой пользователем. Вот код студента:

BRUCE_WILLIS = 42
input_data = input('Введите строку: ')

try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'Leeloo Dallas! Multi-pass № {result}!')
except ValueError as exc:  # as - этот оператор запишет пойманное исключение в переменную exc (название может быть
    # любым)
    print(f'{exc, type(exc)} — невозможно преобразовать к числу')
except IndexError as exc:
    print(f'{exc, type(exc)} — выход за границы списка')
except Exception as exc:
    print(f'{exc, type(exc)} - "поймано исключение')


#Задача 2. Возраст

# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека. Напишите программу,
# которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита) и выводит
# результат в новый файл result.txt в формате «имя — возраст». Программа должна обрабатывать следующие ошибки и
# выводить сообщение на экран: Попытка создания файла, который уже существует. На чтение ожидался файл,
# но это оказалась директория. Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково). При
# желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

file_ages = None
file_result = None

try:
    file_ages = open("ages.txt", "r", encoding="utf8")
    file_result = open("result.txt", "x", encoding="utf8")
    # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
except (FileExistsError, PermissionError) as exc:  # названия исключений можно группировать в кортежи
    print(f'{exc, type(exc)} - Поймано исключение ')
except FileNotFoundError as exc:
    print(f'{exc, type(exc)} - Файл не найден ')

if file_result and file_ages:
    names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    count = 0
    for line in file_ages:
        try:
            clear_line = line.rstrip()
            int(clear_line)  # на всякий случай пытаемся преобразить данные в int, но не сохраняем это в переменную, т.к. записывать нам
            # в файл придётся именно строку
            file_result.write(names[count] + ' - ' + clear_line + '\n')
            count += 1
        except (ValueError, TypeError) as exc:
            print(f'{exc, type(exc)} - Поймано исключение ')


# Задача 1. Простая программа Напишите программу, которая открывает файл и записывает туда введённую пользователем
# строку. Используйте операторы try except else finally. Обработайте возможные ошибки: Проблема при открытии файла.
# Нельзя преобразовать данные в целое. Неожиданная ошибка.