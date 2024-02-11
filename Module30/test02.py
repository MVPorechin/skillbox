from functools import reduce
from typing import List


# Задача 1. Однострочный код Пользователь вводит неопределённое количество чисел. Напишите код, который запрашивает
# эти числа и сортирует их по возрастанию. Реализуйте решение в одну строку.

# nums: List[int] = sorted(list(map(int, input('Введите числа: ').split())))
# print(nums)
# Задача 2. Однострочный код 2 Пользователь вводит строку, состоящую из любых символов. Напишите код, который выводит
# на экран список этих символов, исключая цифры и буквы в верхнем регистре.

# Введите строку: qWe456rtY
# ['q', 'e', 'r', 't']

# list_sym: List[int] = list(filter(lambda x: not (x.isupper() or x.isdigit()), input('Введите строку: ')))
# print(list_sym)
# Задача 3. Функция reduce Помимо map и filter, есть ещё одна функция — reduce. Она применяет указанную функцию к
# элементам последовательности, сводя её к единственному значению. Однако используют reduce довольно редко. Начиная с
# третьей версии Python, эту функцию даже вынесли из встроенных функций в модуль functools.

# Пример кода с reduce:


def my_add(a: int, b: int) -> int:
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


numbers: List[int] = [0, 1, 2, 3, 4]
print(reduce(my_add, numbers))

# Результат:
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10
#
# Используя функцию reduce, реализуйте код, который считает, сколько раз слово was  встречается в списке:

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]


def check_was(a, b):
    if isinstance(a, str):
        a = int(a.count('was'))
    result = a + int(b.count('was'))
    return result


print(reduce(check_was, sentences))