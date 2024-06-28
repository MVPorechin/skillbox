import functools
from typing import Callable, Any


class Date:
    """
    Класс дата, включает себя методы:
        проверять числа даты на корректность;
        конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
    """
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self._day = day
        self._month = month
        self._year = year

    def __str__(self) -> str:
        """
        Выводим на экран полученные данные о дате
        :return: str
        """
        return f'День: {self._day}\tМесяц: {self._month}\t Год: {self._year}'

    @classmethod
    def is_date_valid(cls, text: str) -> bool:
        """
        Метод проверки является ли строка датой
        :param text:
        :return: bool
        """
        day, month, year = map(int, text.split('-'))
        return 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999

    @classmethod
    def from_string(cls, text: str) -> 'Date':
        """
        Метод перевода строки в число, на вход подаем строку, и переводим каждое значение в целое число
        :param text: str
        :return: object
        """
        day, month, year = map(int, text.split('-'))
        dmy_obj = cls(day, month, year)
        return dmy_obj


if __name__ == '__main__':
    date = Date.from_string('10-12-2077')
    print(date)
    print(Date.is_date_valid('10-12-2077'))
    print(Date.is_date_valid('40-12-2077'))

# зачет!
