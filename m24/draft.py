import random


# class User:
#     user_name = 'Admin'
#     password = 'querty'
#     is_banned = False
#
#
# user_1 = User()  # экземлпяр класса User
#
# # user_1.user_name = 'Tom'
# # print(user_1.user_name)
# # user_2 = User()
# # print(user_2.user_name)
# user_2 = User()
# user_2.user_name = 'Tom'
# print(user_1.user_name, user_2.user_name)
# User.user_name = 'noname'
# print(user_1.user_name, user_2.user_name)


# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
# class Toyota:
#     color_auto = 'Red'
#     price = '1000000'
#     max_speed = 200
#     cur_speed = 0
#
#
# cars = [Toyota() for _ in range(3)]
# for index, number in enumerate(cars):
#     cars[index].cur_speed = random.randint(0, 200)

# print(cars[0].cur_speed, cars[1].cur_speed, cars[2].cur_speed)

# Задача 2. Однотипные объекты В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора
# есть четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана. Все четыре
# монитора отличаются только частотой.
#
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в
# наличии микрофона.


class Display:
    display_name = 'AOC'
    display_matrix = 'IPS'
    display_res = '4k'
    display_freq = 144


class Headphones:
    headphones_name = 'Marshall'
    headphones_micro = True
    headphones_sensitivity = 108


monitors = [Display() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]
for index, number in enumerate([60, 144, 70, 50]):
    monitors[index].display_freq = number

headphones[0].headphones_micro = False


class User:
    user_name = 'Admin'
    password = 'querty'
    is_banned = False
    friends = []

    def print_info(self):
        print('Name:{}\nPassword: {}\nBan Status: {}\n'.format(
            self.user_name, self.password, self.is_banned)
        )

    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.user_name)
        else:
            self.friends.append(friend)


user_1 = User()  # экземлпяр класса User
# user_1.print_info()
user_1.add_friend('ivan')
user_2 = User()
user_2.user_name = 'Natasha'
user_1.add_friend(user_2)


# print(user_1.friends)


class Family:
    surname = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print('Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
            self.surname, self.money, self.have_a_house
        )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Currient value: {}'.format(amount, self.money))

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Currient money: {}\n'.format(self.money))
        else:
            print('Not enough money!\n')


my_family = Family()
my_family.info()
print('try to buy a house')
my_family.buy_house(10 ** 6)
if not my_family.have_a_house:
    my_family.earn_money(800000)
    print('Try to buy a house again')
    my_family.buy_house(10 ** 6, 10)

my_family.info()


class Toyota:
    color_auto = 'Red'
    price = 1e6
    max_speed = 200
    cur_speed = 0

    def info(self):
        print(f'Color auto: {self.color_auto}\n'
              f'Price: {self.price}\n'
              f'Maximum speed: {self.max_speed}\n'
              f'Currient speed: {self.cur_speed}\n')

    def set_curr_speed(self, speed):
        self.cur_speed = speed


car_1 = Toyota()
car_1.info()
car_1.set_curr_speed(123)
car_1.info()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        print(
            f'Name: {self.name}\n'
            f'Salary: {self.salary}\n'
        )


emp1 = Employee('Tom', 1e4)
emp2 = Employee('Bob', 2e4)
emp1.print_info()
emp2.print_info()


# Веселая ферма
class Potapo:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False
    def print_state(self):
        print(f'Картошка {index} в стадии {Potapo.states[self.state]}')


class PotapoGarden:
    def __init__(self, count):
        self.potatoes = [Potapo(index) for index in range(1, count + 1)]

    def grow_all(self):
        print(f'картошка прорастает!')
        for i_potapo in self.potatoes:
            i_potapo.grow()

    def are_all_ripe(self):
        if not all([i_potapo.is_ripe() for i_potapo in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела! можно собирать')


my_garden = PotapoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()