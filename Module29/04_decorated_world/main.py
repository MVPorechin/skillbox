import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Функция декоратор. Расширяет функционал декоратора через произвольные аргументы
    :param decorator:
    :return:
    """
    def decorator_create(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_create


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """
    Декоратор для функции
    :param _function_d: передаваемая функция
    :param args:
    :param kwargs:
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101

# зачет!
