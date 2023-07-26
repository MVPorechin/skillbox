import time
from typing import Callable, Any


def timer(func: Callable, *args, **kwargs) -> Any:
    """
    Функция-таймер. Выводит время работы функции и возвращает ее результат
    :param func: передаваемая функция
    :return: Время в секундах
    """
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_at, 4)
    print(f'Функция работала {run_time} секудн(ы)')


def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result


my_result = timer(squares_sum)
print(my_result)
my_cubes_sum = timer(cubes_sum, 200)
print(my_cubes_sum)