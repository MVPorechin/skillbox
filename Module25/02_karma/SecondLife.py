import random


class Karma:
    """
    Базовый класс, описывающий карму.

    __karma_point(int): очки кармы, постоянное число равное 500
    __current_karma_point(int) = текущее значение кармы
    Args:
        __value(int): передается текущие очки кармы
        __list_exception(list): список с исключениями
    """

    __karma_point = 500
    __current_karma_point = 0

    def __init__(self, value):
        self.set_karma(value)
        self.__list_exception = [KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]

    def __str__(self):
        return f'Очки кармы: {self.__current_karma_point}'

    def get_karma(self):
        """
        :return: Возвращает текущее количество кармы
        """
        return self.__current_karma_point

    def set_karma(self, value):
        """
        Метод увеличивает карму на значение передаваемое в аргументе value
        :param value: значение очков кармы возвращенное от self.one_day
        """
        self.__current_karma_point += value

    def one_day(self):
        """
        Метод расчета кармы за один день
        Attributes:
            __one_day_karma(int): случайное число от 1 до 7.
        :return:в случае если вероятность 1 к 10, возвращает кортеж состоящий из значения от 1 до 7,
        и случайное исключение хранящиеся в self.__list_exception иначе только значение от 1 до 7.
        """
        __one_day_karma = random.randint(1, 7)
        self.set_karma(__one_day_karma)
        if random.randint(1, 10) == 10:
            exc = Exception(random.choice(self.__list_exception))
            return __one_day_karma, exc
        else:
            return __one_day_karma


class KillError(Exception):
    """
    Класс Ошибка-Смерть, родитель Исключение.
    """

    def __str__(self):
        return "Жизнь бессмертна, Цель жизни - смерть."


class DrunkError(Exception):
    """
    Класс Ошибка-Пьяный, родитель Исключение.
    """

    def __str__(self):
        return "Вечно молодой, Вечно Пьяный"


class CarCrashError(Exception):
    """
    Класс Ошибка-Автомобильная авария, родитель Исключение.
    """

    def __str__(self):
        return "Если когда-нибудь скорость убьет меня, не плачьте, потому что Я в тот момент улыбался"


class GluttonyError(Exception):
    """
    Класс Ошибка-Обжорство, родитель Исключение.
    """

    def __str__(self):
        return "Обжорство"


class DepressionError(Exception):
    """
        Класс Ошибка-Депрессия, родитель Исключение.
    """

    def __str__(self):
        return "ВСЕ ХОРОШО!? нет"
