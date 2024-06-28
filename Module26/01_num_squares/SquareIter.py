from _collections_abc import Iterable


class SquareIterator:
    """
    Класс возвращающий квадраты от 1 до заданного числа number (1 ** 2 .. number ** 2)

    Arguments:
        number(int): число до какого необходимо посчитать квадрат числа
    """

    __my_var = 0
    _new_var = 1
    def __init__(self, number: int):
        self.__number = number
        self.__value = 0
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.__count += 1
        if self.__number > self.__count:
            self.square_by_class_iter()
            return self.__value
        else:
            raise StopIteration

    def get_number(self) -> int:
        """
        Геттер, возвращает число заданное пользователем
        :return: (int)
        """
        return self.__number

    def square_by_class_iter(self) -> None:
        """
        Метод возводит во 2ую степень число
        """
        self.__value = self.__count ** 2

    def function_generator(self) -> int:
        """
        Метод возводит во 2ую степень число - функция-генератор
            :yield: возвращает число возведенное во 2ую степень
        """
        for _ in range(1, self.__number + 1):
            yield self.__number ** 2

    def expression_generator(self) -> Iterable[int]:
        """
        Метод возводит во 2ую степень число - генераторное выражение
            :return: возвращает генератор
        """
        return (number ** 2 for number in range(1, self.__number + 1))




