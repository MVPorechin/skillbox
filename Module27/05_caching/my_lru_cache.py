from typing import Callable, Any
from functools import wraps
import time


def my_lru_cache_decorator(func: Callable) -> Callable:
    """
    Кэширующий декоратор.
    Если имеется ключ value в словаре, то возвращаем значение от ключа,
    иначе выполняем функцию и добавляем в словарь ключ value и результат от функции в значение ключа..
    :param func: Передаваемая функция
    :return: результат
    """
    @wraps(func)
    def wrapped_func(value: int) -> Any:
        if value in lru_dict.keys():
            return lru_dict[value]
        else:
            result = func(value)
            lru_dict[value] = result
        return result

    lru_dict = dict()
    return wrapped_func


class MyLRUCacheDecorator(dict):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


def timer(func: Callable) -> Callable:
    """
    Декоратор секундомер. Позволяет замерить сколько времени выполняется функция
    :param func: Передаваемая функция
    :return: результат
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        diff_time = end_time - start_time
        print(f'Функция отработала за {diff_time} сек')
        return result
    return wrapped_func