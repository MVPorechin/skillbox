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


class VaccumCleaningRobot(Robot):
    def __init__(self, gun, model, depth):
        super().__init__(gun, model)
        self.depth = depth

    def operate(self):
        print('Робот пылесосит пол')


class SubmarineRobot(WarRobot):
    def __init__(self, gun, model, depth):
        super().__init__(gun, model)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f'Охрана ведется под водой на глубине: {self.depth}')


robot = Robot('X61')
war_robot = WarRobot('blaster', 'Avrora')
war_robot.operate()
vaccum_cleaning_robot = VaccumCleaningRobot('laser', 'Thomas', 10)
vaccum_cleaning_robot.operate()
