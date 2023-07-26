##Декораторы

import time
from typing import Callable, Any

# def decorator(func):
#     def wrapped_func(*args, **kwargs):
#         #код до вызова функции
#         value = func(*args, **kwargs)
#         #код после вызова функции
#         return value
#     return wrapped_func


# @decorator
# def some_function(*args):
#     pass


def timer(func: Callable) -> Callable:
    """
    Декоратор. Выводящий время, которое заняло выполнение декорируемой функции
    """
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print(f'Функция работала {run_time} секунд(ы)')
        return result
    return wrapped_func

@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result

@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result


my_result = squares_sum()
print(my_result)

my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)