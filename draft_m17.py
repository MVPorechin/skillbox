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
# squad_2 = [random.randint(30, 60) for _ in range(10)]
# squad_3_condition = [('Погиб' if squad_1[i_damage] + squad_2[i_damage] > 100
#                       else 'Выжил')
#                      for i_damage in range(10)]
#
# print(f'Урон от первого отряда: {squad_1}')
# print(f'Урон от первого отряда: {squad_2}')
# print(f'Состояние третьего отряда: {squad_3_condition}')

nums = [x for x in range(1, 101) if x % 10 == 0]
new_nums = nums[:]
# new_nums[3] = 0
print(new_nums[3:])  # от 3 индекса
print(new_nums[:5])  # до 5 индекса
print(new_nums[2:5])  # от 2 до 5 индекса
# for i_elem in range(2, 8):
#     print(nums[i_elem], end = ' ')
#
# print('')
#
# for i_elem in range(2, 8):
#     print(new_nums[i_elem], end = ' ')

print(f'{new_nums[2:8]}')
