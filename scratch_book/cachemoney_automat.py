import time


class Timer:
    def __init__(self) -> None:
        print('начало сессии')
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(time.time() - self.start)
        print('конец сессии')
        # if exc_type is TypeError:
        #     return True
        return True


class File(Timer):
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
    log = File(filename='log', mode='a')
    with log as log_file:
        log_file.write(my_atm.show_info())
        log_file.write(my_atm.update_database(user_id='1', balance=500))
        log_file.write(my_atm.update_database(user_id='1', balance=100))
        log_file.write(my_atm.update_database(user_id='2', balance=500))
        log_file.write(my_atm.update_database(user_id='2', balance=100))
        log_file.write(my_atm.authorization(user_id='2'))
        log_file.write(my_atm.authorization(user_id='1'))
