from typing import Callable
app = {}


def callback(key: str):
    """
    Декоратор, формирует хеш функцию, где ключ это имя функции, а значение это функция.
    :param key:
    :return:
    """
    def wrapped(func: Callable):
        app[key] = func

    return wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачет!
