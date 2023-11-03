class CacheMoneyMachine:
    """
    Класс описывающий банкомат
    v0.01
    """

    def __init__(self, name: str, database:dict, location:str, owner:str) -> None:
        self._name = None
        self._database = dict()
        self._location = None
        self._owner = None

    @property
    def info(self):
        return self._name

    @info.setter
    def name(self, name: str) -> None:
        self._name = name

    def authorization(self, user_id: int):
        if user_id in self._database.keys():
            print(f'Привет, {user_id}!\n')
            select = int(input('снять - 1\nпополнить - 2\nбаланс - 3\nподключить автоплатеж - 4\n перевести - 5\nвыход - 0'))
            if select == 0 or select not in [1,2,3,4,5]:
                return 0
            elif select == 1:
                self.eject_money(user_id=user_id, amount=amount)
            elif select == 2:
                self.insert_money(user_id=user_id, amount=amount)
            elif select == 3:
                print(f'Баланс {self._database.get(user_id)}')
            elif select == 4:
                self.connect_autopayment(user_id=user_id)
            elif select == 5:
                self.transfer_money(user_id=user_id)


        else:
            print(f'Пользователь {user_id} не найден')

    def insert_money(self, amount:int):