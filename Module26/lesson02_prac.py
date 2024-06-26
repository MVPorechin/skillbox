# Задача 1. Бесконечный итератор Реализуйте итератор-счётчик, который не принимает никаких атрибутов и имеет только
# один статический атрибут — счётчик. Итератор увеличивает счётчик и возвращает предыдущее значение. У вас должен
# получиться бесконечный итератор. То есть при вызове такого кода в основной программе
#
# my_iter = СountIterator()
#
# for i_elem in my_iter:
#
#     print(i_elem)
#
# значения будут выдаваться бесконечно.
import random


class СountIterator:
    """
    Класс Бесконечный итератор.
    Arguments:
        __count(int) = счетчик
    """

    def __init__(self):
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count_up()
        return self.__count

    def count_up(self):
        self.__count += 1

    def get_count(self):
        return self.__count


my_iter = СountIterator()
# for i_elem in my_iter:
#     print(i_elem)


# Задача 2. Случайная сумма Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента (первый элемент —
# просто случайное вещественное число от 0 до 1). Алексею нельзя хранить в памяти весь этот список, а со значениями
# работать как-то надо. Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу. Также сделайте,
# чтобы при каждом новом вызове итератора в цикле значения считались заново.
#
# Пример работы программы:
#
# Кол-во элементов: 5
#
# Элементы итератора:
# 0.74
# 1.13
# 1.95
# 2.2
# 2.55
#
# Новое кол-во элементов: 6
#
# Элементы итератора:
# 0.79
# 1.58
# 2.55
# 2.81
# 3.06
# 3.34

class SumsOfLastTwo:

    def __init__(self, count):
        self.last = 0
        self.end = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        self.last += random.random()
        return round(self.last, 2)


counter = SumsOfLastTwo(6)
for i in counter:
    print(i)
print("*" * 50)

# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
#
# Основной код:
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47


class Primes:

    def __init__(self, n):
        self.n = n
        self.i = 1
        self.prime_number = []

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        while self.i <= self.n:
            self.i += 1
            for prime in self.prime_number:
                if self.i % prime == 0:
                    break
            else:
                self.prime_number.append(self.i)
                return self.i
        raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')