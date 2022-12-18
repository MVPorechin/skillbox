import random
# tuple
# Задача 1. Создание кортежей
# Заполните, один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав тем самым третий кортеж. С помощью
# метода кортежа определите в нём количество нулей. Выведите на экран третий кортеж и количество нулей в нём.
first_tuple = tuple(random.randint(0, 5) for number in range(5))
second_tuple = tuple(random.randint(-5, 0) for number in range(5))
triple_tuple = tuple(set(first_tuple + second_tuple))
print(f'Результат: {triple_tuple}, кол-во 0 в кортеже: {triple_tuple.count(0)}')