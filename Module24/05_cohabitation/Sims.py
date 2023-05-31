class Human:
    def __init__(self, name='Ivan', satiety=50, house='пр.Дубровка д.35'):
        self.name = name
        self.satiety = satiety
        self.house = house
        self.condition = True

    def __str__(self):
        return f'Имя: {self.name}\nСытость: {self.satiety}\nПроживает: {self.house}\n'

    def to_eat(self, refrigerator):
        refrigerator.meal -= 5
        self.satiety += 10

    def work(self, furniture):
        self.satiety -= 10
        furniture.money += 10

    def play_games(self):
        self.satiety -= 5

    def go_to_store_for_food(self, refrigerator, furniture):
        refrigerator.meal += 30
        furniture.money -= 10
        self.satiety -= 10


class House:
    list_residents = list()
    list_furniture = list()

    def __init__(self, address='ул. Мира д.1'):
        self.address = address

    def __str__(self):
        return f'Дом по адресу: {self.address}\n' \
               f'Проживает: {len(self.list_residents)} человек\n' \
               f'Список проживающих: {self.list_residents}\n'

    def add_residents(self, human):
        self.list_residents.append(human)

    def add_furniture(self, other):
        self.list_furniture.append(other)


class Locker:
    def __init__(self, location=None, money=50):
        self.location = location
        self.money = money

    def __str__(self):
        return f'В тумбочке сейчас находится: {self.money} рублей'

    def get_locker(self, set_address):
        self.location = set_address


class Fridge:
    def __init__(self, meal=50, location=None):
        self.meal = meal
        self.location = location

    def __str__(self):
        return f'В холодильнике сейчас находится: {self.meal} еды'

    def get_fridge(self, set_address):
        self.location = set_address
