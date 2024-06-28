import functools
import time
from typing import Callable, Any


def delay_4_func(func: Callable) -> Callable:
    """
    Декоратор который перед выполнением
    декорируемой функции ждёт несколько секунд
    """
    @functools.wraps(func)
    def wrapped_func(delay: int) -> Any:
        start_delay = time.time()
        end_time = 0
        print(f'отчет пошел')
        while end_time < delay:
            current_time = time.time()
            end_time = current_time - start_delay
        print('отчет закончился')
        return func(delay)

    return wrapped_func


@delay_4_func
def monitoring_web(delay: int) -> str:
    """
    Функция проверяет обновиться ли значения на сайте
    :return:
    """
    print(f'Прошло {delay} секунд(ы), данные не обновились')


monitoring_web(delay=5)

# зачет!
