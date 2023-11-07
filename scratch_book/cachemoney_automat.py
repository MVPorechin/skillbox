import time
import functools
from datetime import datetime
from typing import Callable, Any


def create_time(cls):
    """
    Декоратор класс. Выводит время создания инстранса класса
    :param cls:
    :return:
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'Время создания инстанса класса: {datetime.now()}')
        return instance
    return wrapper


def timer(func: Callable) -> Any:
    """
    Функция-таймер. Выводит время работы функции и возвращает ее результат
    :param func: передаваемая функция
    :return: Время в секундах
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = ended_at - started_at
        print(f'Функция работала {run_time} секудн(ы)')
        return result
    return wrapped


def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его ко всем методам класса
    :param decorator:
    :return:
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


class File:
    """
    Контекст менеджер
    при попытке открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи;
    на выходе из менеджера подавляются все исключения, связанные с файлами
    """

    def __init__(self, filename: str, mode: str) -> None:
        self._filename = filename
        self._mode = mode
        self._file = None

    def __enter__(self) -> None:
        try:
            self._file = open(filename=self._filename, mode=self._mode, encoding='utf-8')
        except IOError:
            self._file = open(filename=self._filename, mode="w", encoding='utf-8')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is IOError:
            self._file.close()
            return True
        else:
            self._file.close()


@create_time
@for_all_methods(timer)
class CacheMoneyMachine:
    """
    Класс описывающий банкомат
    v0.01
    """

    def __init__(self) -> None:
        self._location = None
        self._name = None
        self._database = dict()
        self._owner = None

    def __str__(self):
        return (f'Владелец: {self._owner}\n'
                f'Местоположение: {self._location}\n'
                f'Имя устройства: {self._name}')

    def show_info(self):
        return self._owner, self._location, self._name

    def first_start(self, owner, location, name):
        self._owner = owner
        self._location = location
        self._name = name

    def authorization(self, user_id: int):
        if user_id in self._database.keys():
            print(f'Привет, {user_id}!\n')
            select = int(input('снять - 1\n'
                               'пополнить - 2\n'
                               'баланс - 3\n'
                               'подключить автоплатеж - 4\n'
                               'перевести -  5\n'
                               'выход - 0\n: '))
            if select == 0 or select not in [1, 2, 3, 4, 5]:
                return 0
            elif select == 1:
                self.eject_money(user_id=user_id)
            elif select == 2:
                self.insert_money(user_id=user_id)
            elif select == 3:
                print(f'Баланс {self._database.get(user_id)}')
            elif select == 4:
                self.connect_autopayment(user_id=user_id)
            elif select == 5:
                self.transfer_money(user_id=user_id)
        else:
            print(f'Пользователь {user_id} не найден')

    def insert_money(self, user_id) -> object:
        amount = int(input('Внесите деньги в купюроприемник: '))
        self._database[user_id] = amount + self._database.get(user_id)

    def transfer_money(self, user_id):
        recipient = input('Введите идентификатор получателя: ')
        if recipient in self._database:
            amount = int(input(f'Введите сумму для перевода {recipient}: '))
            if self._database.get(user_id) > 0:
                self._database[user_id] = self._database.get(user_id) - amount
                self._database[recipient] = amount + self._database.get(recipient)
            else:
                print('У вас не достаточно средств')
        else:
            print(f'Пользователь {recipient} не найден')

    def eject_money(self, user_id):
        amount = int(input('Введите сумму для снятия: '))
        self._database[user_id] = self._database.get(user_id) - amount

    def update_database(self, user_id, balance):
        if user_id in self._database:
            self._database[user_id] = balance + self._database.get(user_id)
        else:
            self._database[user_id] = balance


if __name__ == '__main__':
    my_atm = CacheMoneyMachine()
    my_atm.first_start(owner='gref german', location='99.0000000, 66.000000', name='alexander')
    my_atm.show_info()
    my_atm.update_database(user_id='1', balance=500)
    my_atm.update_database(user_id='1', balance=100)
    my_atm.update_database(user_id='2', balance=500)
    my_atm.update_database(user_id='2', balance=100)
    my_atm.authorization(user_id='2')
    my_atm.authorization(user_id='1')
