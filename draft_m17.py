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

print('17.1 - Задача 3. Повышение цен')

# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать, мы спрогнозировали, что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.
# Напишите программу, которая получает на вход список цен на товары (вещественные числа, список генерируется также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.

prices = [float(input("Цена на товар: ")) for _ in range(5)]

first_year = int(input("Повышение на первый год: "))
second_year = int(input("Повышение на второй год: "))

all_prices = "Сумма цен за каждый год: "
for percent in 0, first_year, second_year:
    prices = [price * (1 + percent / 100) for price in prices]
    all_prices += f" {round(sum(prices), 2)}"

print(all_prices)