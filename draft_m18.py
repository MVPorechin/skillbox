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

# print('Задача 1. Улучшенная лингвистика 2')
# Усовершенствуйте старую программу:
# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения,
# который вводится уже в одну строку. Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.
#
# words = [input("Введите слово: ") for _ in range(3)]
# text = input("Введите текст: ")
# words_count = [text.count(word) for word in words]
# print(f'{words_count}')

# print('Задача 2. Бабушка')
# У одной бабушки, когда та переписывается с внуком, постоянно залипает кнопка пробела.
# В итоге между словами получаются огромные расстояния.
# Внук не знает как это поправить в самом телефоне, поэтому обратился к вам за помощью.
# Пользователь вводит строку. Напишите программу, которая преобразовывает
# в этой строке все идущие подряд пробелы в один и выводит результат на экран.
# Пример:
# Введите текст: У       нас         пошёл                    снег    !
# Исправленный текст: У нас пошёл снег !
# text = input("Введите текст: ")
# print(" ".join(text.split()))

# print('Задача 3. Разделители символов')
# Человек хочет сделать рассылку поздравлений для определённого списка людей. Поздравления для разных людей он хочет написать по-разному.
#
# Напишите программу, которая запрашивает у пользователя:
# Шаблон поздравления (туда вставляется ФИ и возраст)
# ФИ людей (в одну строку, разделяются запятой)
# Возраст каждого человека (в одну строку через пробел)
# В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.
# Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: С днём рождения, {name}! С {age}-летием тебя!
# Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
#
# Возраст людей через пробел: 20 30 18
# С днём рождения, Иван Иванов! С 20-летием тебя!
# С днём рождения, Петя Петров! С 30-летием тебя!
# С днём рождения, Лена Ленова! С 18-летием тебя!
# Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18

# while True:
#     grats_template = input("Введите шаблон поздравления, "
#                            "в шаблоне можно использовать конструкцию {name} и {age}: "
#                            "С днём рождения, {name}! С {age}-летием тебя! ")
#     if "{name}" in grats_template and "{age}" in grats_template:
#         break
#     print("Ошибка! Отсутствует одна или несколько конструкций!")
#
# names_list = input("Введите список людей через запятую: ").split(",")
# # если ввод только через запятую то пробел не добавялем, если с пробелом то - .split(", ")
# ages_str = input("Введите возраст людей через пробел: ")
# ages = [int(age) for age in ages_str.split()]
#
# for index, name in enumerate(names_list):
#     print(grats_template.format(name=name, age=ages[index]))

# # Вариант с небольшой долей "магии" (инструмент будет изучен в будущих модулях):
# for age, name in zip(ages, names_list):  # zip соединяет списки и можно брать сразу по элементу из каждого
#     print(grats_template.format(name=name, age=age))

# people = [" ".join([names_list[index], str(ages[index])]) for index in range(len(names_list))]
# print("Именинники:", ", ".join(people))

# user_name = input('Введите имя пользователя: ')
# file_name = input('Введите имя файла: ')
#
# path = 'C:/Users/{user}/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if not path.endswith('.txt'):
#     print('Ошибка: не верное расширение файла')
# elif not path.startswith('C:/'):
#     print('Ошибка: неверно указан диск')
# else:
#     print(f'Путь к файлу: {path}')

# words_list = []
#
# for i_num in range(1, 4):
#     # word = input(f'Введите {i_num} слово: ').lower()
#     word = input(f'Введите {i_num} слово: ').upper()
#
#     words_list.append(word)
#
# # text = input('Введите текст: ').lower().split()
# text = input('Введите текст: ').upper().split()
#
#
# print(f'Подсчет слов в тексте: ')
# for index in range(3):
#     print(f'{words_list[index]} : {text.count(words_list[index])}')

# print('Задача 1. Шифр Цезаря 2')
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.

# print(ord("а"), ord("я"), ord("ё"), chr(1104))
#
# text = input("Введите текст: ")
# delta = int(input("Введите сдвиг: "))
# alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]  # заполняем список буквами алфавита
# # Думаем над структурой алгоритма: [вариант_1 если условие_1 иначе вариант_2 for буква in текст]
# new_text = [alphabet[(alphabet.index(letter) + delta) % len(alphabet)] if letter in alphabet else letter for letter in text.lower()]
# print(''.join(new_text))

# print('Задача 2. Путь к файлу')
# Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта часто используются абсолютные пути файлов, которые необходимо проверять.
# Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные: диск и расширение файла. Напишите программу, которая проверяет корректность этого пути.
#
# user_name = input('Введите имя пользователя: ')
# file_name = input('Введите имя файла: ')
#
# path = 'C:/Users/{user}/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if not path.endswith('.txt'):
#     print('Ошибка: не верное расширение файла')
# elif not path.startswith('C:/'):
#     print('Ошибка: неверно указан диск')
# else:
#     print(f'Путь к файлу: {path}')

# print('Задача 3. Удаление части')
# На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы. Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных. Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все прописными.
# Подсказка: используйте методы islower() и/или isupper().

# input_text = input('Введите строку: ')
# if input_text.islower():
#     print(input_text.upper())
# else:
#     print(input_text.lower())

# text = input("Введите текст: ")
# lowers = len([letter for letter in text if letter.islower()])
# uppers = len([letter for letter in text if letter.isupper()])
#
# if lowers > uppers:
#     print("Результат:", text.lower())
# else:
#     print("Результат:", text.upper())


# details_num = 500000000
# price = 23.34523466
# increase = 0.045636
#
# print('На складе {:,d} деталей'.format(details_num))
# print('Каждая деталь стоит {:.2f} рублей'.format(price))
# print('Цена увеличилась на {:.1%}'.format(increase))
# print('На складе {:.0e} деталей'.format(details_num))


