import functools
from typing import Callable, Optional, Any
from datetime import datetime
import time


def timer(func: Callable) -> Any:
    """
    Функция-декоратор фиксирует и выводит время работы декорируемой функции
    :param func: функция
    :return: функция
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 2)
        print(f'Завершение {func.__qualname__}. Время работы {run_time} секудн(ы)')
        return result

    return wrapped


def logger_with_args(_func: Optional[Callable] = None, *, time_format: str = None) -> Callable:
    """
    Функция-декоратор фиксирует время запуска декорируемой функции
    :param _func: функция
    :param time_format: формат отображения времени
    :return: функция
    """

    def logged(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            print(f"Запускается {func.__qualname__} произошёл в: ", datetime.today().strftime(time_format))
            return func(*args, **kwargs)

        return wrapped

    if time_format is None:
        time_format = '%b %d %Y - %H:%M:%S'
    else:
        convert_time_format = ''
        for sym in time_format:
            if sym.isalpha():
                convert_time_format += '%' + sym
            else:
                convert_time_format += sym
        time_format = convert_time_format

    if _func is None:
        return logged
    else:
        return logged(_func)


def logger(format: str) -> Callable:
    """
    Декоратор функция.
    Декорирует все не магические методы класса
    :param format: формат для отображения формата даты, времени
    :return:
    """
    def decorator(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                curr_method = getattr(cls, i_method)
                decorate_method = logger_with_args(timer(curr_method), time_format=format)
                setattr(cls, i_method, decorate_method)

        return cls
    return decorator


@logger(format="b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@logger(format="b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# - Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# - Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_1
# - Завершение 'A.test_sum_1', время работы = 0.187s
# Тут метод test_sum_1 у наследника
# - Завершение 'B.test_sum_1', время работы = 0.187s
# - Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_2 у наследника
# - Завершение 'B.test_sum_2', время работы = 0.370s

# зачет!
