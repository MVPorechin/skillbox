import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор "шутка"
    :param func: передаваемая функция для декоратора
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        question = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapped_func


@how_are_you
def test():
    """
    Функция для проверки "декоратора-шутки"
    :return(str): Сообщение
    """
    print('<Тут что-то происходит...>')


test()

# зачет!
