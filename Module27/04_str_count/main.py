from typing import Any, Callable
import functools


class CounterDecorator(object):
    """
    Класс для декоратора счетчика
    """
    __count = 0

    def __init__(self, func):
        self.func = func

    def increase_count(self):
        self.__count += 1

    def get_count(self):
        return self.__count

    def __call__(self, *args, **kwargs):
        """
        Декоратор считающий и выводящий количество вызовов декорируемой функции
        :param self: функция для декорирования
        :return:
        """
        self.increase_count()
        self.func(*args, **kwargs)
        print(self.get_count())


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    :param func: декорируемая функция
    :return: вызов декоратора
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        wrapped_func.count += 1
        print(f'Декоратор был запущен {wrapped_func.count} раз')
        return func(*args, **kwargs)

    wrapped_func.count = 0
    return wrapped_func


@CounterDecorator
@counter
def test():
    """
    Функция для проверки "декоратора-шутки"
    :return(str): Сообщение
    """
    print('<Тут что-то происходит...>')


#1
test()
#2
test()
#3
test()
#4
test()

# зачет!
