# Задача 1. Повторение кода
#
# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.
#
#
#

def do_nice(n):
    def wrap_fun(func):
        """декоратор do_twice, который дважды вызывает декорируемую функцию"""

        def wrapped_func(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return

        return wrapped_func

    return wrap_fun


@do_nice(5)
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

from time import sleep


def slow_it_now(_func=None, *, n=1):
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
    Проверка декоратора и вывод прстого сообщения

    :return:
    """
    print('<Тут что-то происходит...>')


test()
