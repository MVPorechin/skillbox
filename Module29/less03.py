import functools
import time
from typing import Callable, Any, Optional


def timer_with_precision(_func: Optional[Callable] = None, *, precision: int = 10) -> Callable:
    def timer_decorator(func: Callable) -> Any:
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
            run_time = round(ended_at - started_at, precision)
            print(f'Функция работала {run_time} секудн(ы)')
            return result
        return wrapped
    if _func is None:
        return timer_decorator
    return timer_decorator(_func)


@timer_with_precision
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


@timer_with_precision(precision=4)
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result


my_result = squares_sum
print(my_result)
my_cubes_sum = cubes_sum(number=200)
print(my_cubes_sum)