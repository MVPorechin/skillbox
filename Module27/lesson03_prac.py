# Задача 1. Сэндвич
# Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут различные
# ингредиенты вроде салата, помидоров и других. Всё это в свою очередь содержится между двух половинок булочки.
# Реализуйте такую функцию и два соответствующих декоратора — ингредиенты и хлеб.
#
# Пример результата работы программы при вызове функции sandwich:
from typing import Callable, Any


# </----------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

def bread(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        print('</----------\>')
        func(*args, **kwargs)
        print('<\______/>')

    return wrapped_func


def ingredients(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        print('#помидоры#')
        func(*args, **kwargs)
        print('~салат~')

    return wrapped_func


@bread
@ingredients
def burger(meat: str) -> Any:
    print(meat)


burger(meat='--ветчина--')


# Задача 2. Плагины
# Один проект состоит из огромного количества разнообразных функций, часть из которых используется
# в других проектах в качестве плагинов, то есть они как бы «подключаются» и создают дополнительный функционал.
#
# Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как плагины и заносить их в
# соответствующий словарь.

from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()


def register(func: Callable) -> Callable:
    """    Декоратор регистрирует функцию как плагин    """
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return 'Hello {name}'.format(name=name)


@register
def say_goodbye(name: str) -> str:
    return 'Goodbye {name}'.format(name=name)


print(PLUGINS)
print(say_hello('Tom'))




plugins = {}


def go_to_plugins(func):
    plugins[func.__name__] = func
    return func


@go_to_plugins
def hello():
    print('Hello!')

print(plugins)
