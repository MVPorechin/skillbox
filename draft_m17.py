# print('List comprehensions')
# squares = [x ** 2 for x in range(10)]
# print(f'{squares}\n')
#
#
# def get_higher_price(percent, price):
#     return round(price * (1 + percent / 100), 2)
#
#
# prices_now = [1.9, 22.34, 56.3, 52.9, 88.5, 99.4]
# first_percent = int(input('Повышение на первый год: '))
# second_percent = int(input('Повышение на второй год: '))
# prices_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
# prices_second = [get_higher_price(second_percent, i_price)for i_price in prices_first]
#
# print(f'Сумма цен за каждый год {round(sum(prices_now), 2), round(sum(prices_first), 2), round(sum(prices_second), 2)}')

# print('17.1 - Задача 1. Кубы и квадраты')
# Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка: в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом же диапазоне. Выведите списки на экран. Для генерации используйте list comprehensions (как и в следующих задачах).
# left_limit = int(input('Левая граница: '))
# right_limit = int(input('Правая граница: '))
# squares = [x ** 2 for x in range(left_limit, right_limit + 1)]
# cubes = [x ** 3 for x in range(left_limit, right_limit + 1)]
# print(f'Список кубов чисел в диапазоне от {left_limit} до {right_limit}: {cubes}')
# print(f'Список квадратов чисел в диапазоне от {left_limit} до {right_limit}: {squares}')

# print('17.1 - Задача 2. Сообщение')
# Илья решил безобидно подшутить над другом и написал программу для смартфона, которая при отправке сообщения удваивает каждый символ строки и заодно к каждому удвоенному добавляет ещё один дополнительный.
# Пользователь вводит строку и дополнительный символ. Напишите программу, которая генерирует два списка: в первом списке каждый элемент — удвоенная буква первой строки, во втором списке каждый элемент — конкатенация элемента первого списка и дополнительного символа.
# word = input('Введите строку: ')
# word_special_symbol = input('Введите дополнительный символ: ')
# word_list = [abc + abc for abc in word]
# word_list_special = [abc + abc + word_special_symbol for abc in word]
# print(f'{word_list}')
# print(f'{word_list_special}')

# print('17.1 - Задача 3. Повышение цен')

# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать, мы спрогнозировали, что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.
# Напишите программу, которая получает на вход список цен на товары (вещественные числа, список генерируется также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.

# prices = [float(input('Цена за товар :')) for _ in range(5)]
# first_year_percent = int(input('Повышение на первый год: '))
# second_year_percent = int(input('Повышение на второй год: '))
#
# result_prices = []
# for percent in 0, first_year_percent, second_year_percent:
#     prices = [price * (1 + percent / 100) for price in prices]
#     result_prices.append(round(sum(prices), 2))
#
# print(f'Сумма цен за каждый год: {result_prices}')


# squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]
# squares_cubes = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10)]
#
# print(f'{squares_odds}\n')
# print(f'{squares_cubes}\n')
#


# print('17.2 - Задача 1. Список чётных чисел')
# Пользователь вводит два числа: А и В. Реализуйте код, который генерирует список из чётных чисел в диапазоне от А до B. Используйте list comprehensions (как и в следующих задачах).
# numbers_a = int(input('Введите число А: '))
# numbers_b = int(input('Введите число В: '))
# condition = [random.randint(numbers_a, numbers_b) % 2 == 0 for _ in range(numbers_a, numbers_b +1)]
# # result = [condition[_] % 2 == 0 for _ in range(numbers_a, numbers_b)]
#
# print(f'Результат от {numbers_a} до {numbers_b} : {condition}')

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# prices = [price if price > 0 else 0 for price in original_prices]
# print(f'Результат : {prices}')

# print('17.4 - Задача 3. Отряды')
# Мы продолжаем пробовать себя в качестве разработчика игр. Теперь нужно написать небольшую логику поведения некоторых отрядов, а также их урон. Есть два отряда, в каждом по 10 монстров. В первом отряде у каждого монстра урон абсолютно случайный и колеблется от 50 до 80, а во втором — от 30 до 60. Оба отряда вместе напали на третий, также из 10 юнитов. Юнит третьего отряда погибает, если сумма урона от двух монстров больше 100.
#
# Напишите программу, которая генерирует случайные значения в первых двух списках в заданных диапазонах, а также генерирует список, состоящий из фраз «Погиб» или «Выжил». Выведите все списки на экран.
# import random
#
# squad_1 = [random.randint(50, 80) for _ in range(10)]
# squad_2 = [random.randint     for i_damage in range(10)]
#(30, 60) for _ in range(10)]
# squad_3_condition = [('Погиб' if squad_1[i_damage] + squad_2[i_damage] > 100
#                       else 'Выжил')
#
# print(f'Урон от первого отряда: {squad_1}')
# print(f'Урон от первого отряда: {squad_2}')
# print(f'Состояние третьего отряда: {squad_3_condition}')

# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
# print(new_nums[:])
# print(new_nums[3:])  # от 3 индекса
# print(new_nums[:5])  # до 5 индекса
# print(new_nums[2:5])  # от 2 до 5 индекса
# for i_elem in range(2, 8):
#     print(nums[i_elem], end = ' ')
#
# print('')
#
# for i_elem in range(2, 8):
#     print(new_nums[i_elem], end = ' ')
#
# print(f'{new_nums[2:8]}')

# nums[2:8:2]  # от 2 до 8 индекс, с шагом 2
# nums[::-1]  # перевернуть список - "отзеркалить"

# start_sequence = [1, 2, 3, 4, 5]
# finish_sequence = []
# count_sequence = int(input('Кол-во чисел: '))
# for _ in range(1, count_sequence + 1):
#     number = int(input('Число: '))
#     start_sequence.append(number)
# print(f'Последовательность: {start_sequence}')


# def symmetry(start_sequence):
#     reverse_list = start_sequence[::-1]
#     if start_sequence == reverse_list:
#         return True
#     else:
#         return False
#
#
# for i_nums in range(0, len(start_sequence)):
#     if symmetry(start_sequence[i_nums:len(start_sequence)]):
#         finish_sequence = start_sequence[:i_nums]
#         finish_sequence.reverse()
#         break
#
# print(f'Исходный список:  {start_sequence}')
# print(f'Нужно чисел: {len(finish_sequence)}\nCписок этих чисел: {finish_sequence}')

# print('17.4 - Задача 1. Анализ цен')
# Нашему другу заказали написать программу, которая анализирует цены на бирже. Она получает этот пакет данных, но делать что-либо с ним нельзя. Для нормальной работы аналитической программы берётся новый список, который равен тому, что пришло. Затем идёт работа с новым списком: если есть отрицательные цены, то программа их зануляет и в конце выводит на экран, сколько денег мы по итогу потеряли. Получился вот такой код:
# Однако при таких входных данных программа почему-то работает неправильно: она выводит ответ 0, когда правильный ответ 14. Помогите другу исправить программу, а также сделайте так, чтобы список цен генерировался случайно (диапазон можно выбрать любой)
# import random
# original_prices = [random.randint()]
# new_prices = original_prices[:]
# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
#
# print(f'Мы потеряли: {sum(original_prices) - sum(new_prices)}')

# print('17.4 - Задача 2. Срезы')
# # Дан список чисел:
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# # Напишите программу, которая выводит на экран шесть ответов:
# # Для решения используйте только срезы (и без функции len).
# print(f'{nums[:5]}')  # В первой строке выведите первые пять элементов списка.
# print(f'{nums[:-2]}')  # Во второй строке выведите весь список, кроме последних двух элементов.
# print(f'{nums[::2]}')  # В третьей строке выведите все элементы с чётными индексами.
# print(f'{nums[1::2]}')  # В четвёртой строке выведите все элементы с нечётными индексами.
# print(f'{nums[::-1]}')  # В пятой строке выведите все элементы в обратном порядке.
# print(f'{nums[::-2]}')  # В шестой строке выведите все элементы списка через один в обратном порядке, начиная с последнего.

# print('17.4 - Задача 3. Удаление части')
# # Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B). Напишите программу, которая удаляет элементы списка с индексами от А до В. Не используйте дополнительные переменные и методы списков.
# import random
# long = int(input('Введите длину списка: '))
# first_number = int(input('Введите число А: '))
# second_number = int(input('Введите число B: '))
# if first_number < second_number:
#     nums = [random.randint(-10, 10) for _ in range(long)]
# else:
#     print('Число А должно быть меньше числа В')
#     first_number = int(input('Введите число А заново: '))
#     second_number = int(input('Введите число B заново: '))
# first_number = random.randint(0, len(nums) - 2)
# second_number = random.randint(first_number + 1, len(nums) -1)
#
# print(f'Получаем список : {nums}')
# print(f'Убираем числа с индексом от {first_number} до {second_number}\nРезультат: {nums[:first_number] + nums[second_number + 1:]}')

print('17.5 Строки: индексы и срезы')
word = 'Привет'

first_part = word[:len(word) // 2]
print(first_part[::-1])

second_part = word[:len(word) // 2:]
print(second_part[::-1])

print(first_part[::-1] + second_part[::-1])