from typing import Any, Callable
import functools
import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор, который будет отвечать за логирование функций
    :param Callable:
    :return:
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'Вызываем функцию {func.__name__}\n'
              f'Документация к функции {func.__doc__}\n')
        with open(file='function_errors.log', mode='a', encoding='UTF-8') as function_errors:
            try:
                func(*args, **kwargs)
            except Exception as exc:
                function_errors.write(str(datetime.datetime.now()) + str(type(exc)) + ' ошибка ' + str(exc)+'\n')

    return wrapped_func


@logging
def some_func():
    """
    Функция для проверки логирования
    :return str: возвращает строку
    """
    print('Съешь еще этих французских булок да выпей чаю')


@logging
def some_func_whit_error():
    """
    Функция с ошибкой "деление на ноль"
    :return str: возвращает строку
    """
    calc = 10 / 0
    print('Делить на ноль нельзя')


some_func()
some_func_whit_error()

# зачет!
