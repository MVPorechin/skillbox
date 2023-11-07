from time import sleep


# Задача 1. Повторение кода
#
# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.
#
#
#

def repeat(n):
    def wrap_fun(func):
        """Декоратор repeat, который дважды вызывает декорируемую функцию"""

        def wrapped_func(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return

        return wrapped_func

    return wrap_fun


@repeat(5)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting("hello")


# Задача 2. Замедление кода 2
#
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор,
# который перед выполнением декорируемой функции ждёт несколько секунд.
#
# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
# По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор можно было использовать
# как с аргументами, так и без них.


def slow_it_now(_func=None, *, n: int = 1):
    def slowdown_ns(func):
        def wrapper(*args, **kwargs):
            sleep(n)
            result = func(*args, **kwargs)
            return result

        return wrapper

    if _func is None:
        return slowdown_ns
    else:
        return slowdown_ns(_func)


@slow_it_now
def test() -> None:
    """
    Проверка декоратора и вывод простого сообщения

    :return:
    """
    print('<Тут что-то происходит...>')


test()
