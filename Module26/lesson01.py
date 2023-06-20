import random

class MyIter:
    """

    """

    def __init__(self, iterable):
        """

        :param iter_object:
        """
        self.iterable = iterable
        self.end_iter_object = False


    def loop(self, loop_body_func):
        self.iterator = iter(self.iterable)

        while not self.end_iter_object:
            try:
                elem_from_iterator = next(self.iterator)
            except StopIteration:
                self.end_iter_object = False
            else:
                loop_body_func(elem_from_iterator)


my_list = [1, 2, 3, 4, 5]


iterator = my_list.__iter__()
end_iter = False

while not end_iter:
    try:
        step_iter = iterator.__next__()
        print(step_iter)
    except StopIteration as exc:
        end_iter = True
        print(type(exc), exc)

# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(next(iterator))
# print(next(iterator))

# Задача 1. Свой for (ну почти)
#
# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию,
# которая эмулирует работу цикла for с помощью цикла while и проходит во всем элементам итерируемого объекта.
# Не забудьте про исключение «конца итерации».

n = int(input("Введите количество чисел: "))
numbers = [random.randint(-100, 100) for _ in range(n)]

buffer_iter = iter(numbers)

while True:
    try:
        print(next(buffer_iter))
    except StopIteration:
        print("Конец!")
        break