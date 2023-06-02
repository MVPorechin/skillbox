import os
# Задача 1.
# Корабли Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель,
# и каждый может сделать два действия: сообщить свою модель и идти по воде. Грузовой корабль имеет такой атрибут,
# как заполненность, изначально он равен нулю. У него есть ещё два действия: погрузить и выгрузить груз с корабля. У
# военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью. Также,
# вместо погрузки и выгрузки, у него есть другое действие — атаковать. Реализуйте классы грузового и военного
# кораблей. Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование. Не
# забудьте про функцию super в дочерних классах.

class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f'\nМодель корабля: {self.__model}'

    def sail(self):
        print(f'\nКорабль куда-то поплыл')


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print(f'\nКорабль атакует с помощью оружия {self.gun}')


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('\nЗагружаем корабль')
        self.tonnage_load += 1
        print(f'Текущая загруженность: {self.tonnage_load}')

    def unload(self):
        print('\nРазгружаем корабль')
        if self.tonnage_load > 0:
            self.tonnage_load -= 1
        else:
            print('Корабль уже разгружен')
        print(f'Текущая загруженность: {self.tonnage_load}')


warship = WarShip('Lincore', 'blaster')
warship.attack()
cargoship = CargoShip('Ship-Pips')
cargoship.load()


# Задача 2.
# Роботы На военную базу завезли несколько интересных моделей роботов, которые похожи между собой,
# но имеют немного разные функции. У каждого робота есть номер модели и действие operate, которое означает,
# что делает робот. Особенности роботов следующие:
#
# У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает, что он пылесосит пол, и выводит текущую заполняемость мешка.
# У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта с помощью этого оружия.
# Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины, и при команде operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.
#
# Напишите программу, которая реализует все необходимые классы роботов.
class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class WarRobot(Robot):

    def __init__(self, gun, model):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print(f'Робот охраняет военный обьект при помощи {self.gun}')


class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        print('Робот пылесосит пол')


class SubmarineRobot(WarRobot):

    def __init__(self, gun, model, depth):
        super().__init__(gun, model)
        self.depth = depth

    def operate(self):
        super().operate()
        print('Охрана ведется под водой на глубине', self.depth)


robot = Robot('X61')
robot.operate()
war_robot = WarRobot('railgun', 'Avrora')
war_robot.operate()
vaccum_cleaning_robot = VacuumCleaningRobot(10)
vaccum_cleaning_robot.operate()


# Задача 3. Кастомные исключения
#
# Исключения в Python также являются классами, и все они берут свои истоки от самого главного класса — Exception.
# И для создания своего собственного класса ошибки достаточно написать его дочерний класс. Например:
#
# class MyOwnException(Exception):
#
#     pass
#
# raise MyOwnException('Это моя ошибка!')
#
# Причём содержимое объекта исключения чаще всего так и оставляют (просто pass), чтобы не сломать автоматические обработчики исключений.
# Напишите программу, которая считывает из файла numbers.txt пары чисел, делит первое число на второе и выводит ответ на экран.
# Если первое число меньше второго, то программа выдаёт исключение DivisionError (нельзя делить большее на меньшее).
# Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.
class DivisionError(Exception):
    pass


path_to_file = os.path.abspath('numbers.txt')
with open(path_to_file, 'r') as file_number:
    for line in file_number:
        try:
            clear_line = line.rstrip()
            first, second = clear_line.split()
            if int(first) < int(second):
                raise DivisionError('Нельзя делить большее на меньшее')
        except(ValueError, DivisionError) as exc:
            print(exc, type(exc), first, second)