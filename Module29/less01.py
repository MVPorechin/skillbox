from typing import Iterator
from contextlib import contextmanager


@contextmanager
def next_num(num: int) -> Iterator[int]:
    print('входим  в функцию')
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print(f'обнаружена ошибка: {exc}')
    finally:
        print('тут код выполниться в любом случае')
    print('выход из функции')


with next_num(-1) as next:
    print(f'следующее число: {next}')
    print(10 / next)