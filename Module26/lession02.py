import random


class RandomNumbers:

    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return random.randint(0, 10)
        else:
            raise StopIteration


my_iter = RandomNumbers(limit=3)

# for num in my_iter:
#     print(num)


class Fibonacci:
    """
    Итератор последовательности Фибоначчи из N элементов
    """
    def __init__(self, number):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number

    def __iter__(self):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration()
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val

        return self.cur_val


fib_iter = Fibonacci(10)
for i_value in fib_iter:
    print(i_value)
print(8 in fib_iter)