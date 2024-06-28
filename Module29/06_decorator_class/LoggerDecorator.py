import functools
import time
from typing import Callable


class LoggerDecorator:
    """
    Класс декоратор. Измеряет время выполнения декорируемой функции, аргументы и результат, и выводит на экран
    """

    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Вызов функции: {self.func.__qualname__}')
        print(f'Аргументы: {args, kwargs}')
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f'Результат: {result}')
        print(f'Время выполнения: {end_time} секунд')


# Вызов функции: complex_algorithm
# Аргументы: ((10, 50), {})
# Результат: 14500
# Время выполнения: 0.06757426261901855 секунд
