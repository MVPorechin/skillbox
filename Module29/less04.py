import time
from datetime import datetime
import functools
from typing import Callable, Any


def create_time(cls):
    """
    Декоратор класс. Выводит время создания инстранса класса
    :param cls:
    :return:
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'Время создания инстанса класса: {datetime.now()}')
        return instance
    return wrapper


def timer(func: Callable) -> Any:
    """
    Функция-таймер. Выводит время работы функции и возвращает ее результат
    :param func: передаваемая функция
    :return: Время в секундах
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = ended_at - started_at
        print(f'Функция работала {run_time} секудн(ы)')
        return result
    return wrapped


def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его ко всем методам класса
    :param decorator:
    :return:
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@create_time
@for_all_methods(timer)
class Function:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        numbers = 100
        result = 0
        for _ in range(numbers + 1):
            result += sum([i_num ** 2 for  i_num in range(self.max_num)])

        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])

        return result


my_func_1 = Function(max_num=1000)
# time.sleep(1)
# my_func_2 = Function(max_num=2000)
# time.sleep(1)
# my_func_3 = Function(max_num=3000)
my_func_1.squares_sum()
my_func_1.cubes_sum(number=2000)
