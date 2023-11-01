"""
Декоратор контекст менеджер
пример 1
"""
from contextlib import contextmanager
from collections.abc import Iterator
import time


@contextmanager
def next_num(num: int) -> Iterator[int]:
    print('Входим в функцию')
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print('Обнаружена ошибка', exc)
    finally:
        print('Здесь код выполниться в любом случае')
    print('выход из функции')


with next_num(0) as next:
    print('Следующее число = {}'.format(next))
    print(10 / next)

"""
пример 2
"""

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(time.time() - start)


# class Timer:
#     def __init__(self) -> None:
#         print('Время работы кода')
#         self.start = None
#
#     def __enter__(self) -> 'Timer':
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         print(time.time() - self.start)
#         # if exc_type is TypeError:
#         #     return True
#         return True


with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 1000000
    val_1 += 'sdfg'

with timer() as t2:
    print('Вторая часть')
    val_3 = 200 * 200 ** 2000000

with timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 3000000
