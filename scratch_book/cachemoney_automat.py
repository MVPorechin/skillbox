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
            select = int(input('снять - 1\nпополнить - 2\nбаланс - 3\nподключить автоплатеж - 4\n перевести - '
                               '5\nвыход - 0\n: '))
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


my_atm = CacheMoneyMachine()
my_atm.first_start(owner='gref german', location='99.0000000, 66.000000', name='alexander')
print(my_atm.show_info())
my_atm.update_database(user_id='1', balance=500)
my_atm.update_database(user_id='1', balance=100)
my_atm.update_database(user_id='2', balance=500)
my_atm.update_database(user_id='2', balance=100)
my_atm.authorization(user_id='2')
my_atm.authorization(user_id='1')
