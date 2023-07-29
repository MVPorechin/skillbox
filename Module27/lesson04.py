import time
import functools
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Декоратор. Выводящий время, которое заняло выполнение декорируемой функции
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print(f'Функция работала {run_time} секунд(ы)')
        return result

    return wrapped_func


def logging(func: Callable) -> Callable:
    """
    Декоратор, логирующий работу кода
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('\nВызывается функция: {func}\t'
              'Позиционные аргументы: {args}\t'
              'Именованные аргументы: {kwargs}'.format(
            func=func.__name__, args=args, kwargs=kwargs
        ))
        result = func(*args, **kwargs)
        print('Функция успешно завершила работу')
        return result

    return wrapped_func

@logging
@timer
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов
    для каждого N от 0 до 10000,
    где 0 <= N <= 100
    :return: сумма квадратов
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result

@timer
@logging
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result

print(squares_sum.__doc__)
print(squares_sum.__name__)

