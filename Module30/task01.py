# Задача 1. Счётчик 2 Как-то мы уже создавали декоратор counter, который считает и выводит количество вызовов
# декорируемой функции. Для этого мы использовали интересную особенность классов. В этот раз реализуйте тот же
# декоратор, но уже с использованием знаний о локальных и глобальных переменных. Реализуйте декоратор двумя способами:
#
# используя глобальную переменную count;
# используя локальную переменную count внутри декоратора.
#
# Дополнительно: найдите команду (в интернете или даже сами), которая перечисляет все функции и методы, находящиеся
# во встроенном пространстве имён в Python

global_count = {}


def decorator_counter(func):
    local_count = {}

    def wrapped_func(*args, **kwargs) -> None:
        global global_count
        nonlocal local_count
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        local_count[func.__name__] = local_count.get(func.__name__, 0) + 1
        print(f'global: {global_count},\nlocal: {local_count}')
        return func(*args, **kwargs)

    wrapped_func.check_count = local_count
    return wrapped_func


@decorator_counter
def say_hello():
    print('hello')


@decorator_counter
def say_hello_2():
    print('hello')


say_hello()
say_hello()
say_hello_2()
say_hello_2()
print(say_hello_2.check_count)

print('')
print(dir(__builtins__))