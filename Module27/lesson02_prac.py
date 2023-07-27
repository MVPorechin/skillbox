# Задача 1. Двойной вызов
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию. Не забывайте про документацию и аннотации типов.
import time
from typing import Callable, Any


# Пример декорируемой функции:
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))
# Основной код:
# greeting('Tom')

# Результат:
# Привет, Tom!
# Привет, Tom!

def double_greeting(func: Callable) -> Callable:
    def wrapped(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapped


# Основной код:
@double_greeting
def greeting(name) -> str:
    print('Привет, {name}!'.format(name=name))


# greeting('Tom')


# Задача 2. Таймер 2
# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию,
# которая сделала всю работу за вас, что позволило большую часть времени смотреть видео с котиками в интернете.
# Однако, увидев свой код, вы как программист с опытом поняли, что этот код можно написать намного красивее и удобнее.
#
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран. Для проверки
# примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.

def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        start_t = time.time()

        res_func = func(*args, **kwargs)

        end_t = time.time()
        result_t = end_t - start_t
        print(f'Функция отработала {result_t} секунд')
        return res_func
    return wrapped_func


@timer
def hard_func():
    return [x ** 2 ** x for x in range(22)]


hard_func()
