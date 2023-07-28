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