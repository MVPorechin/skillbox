import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ",
              round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить
        # выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    def __init__(self, name):
        super().__init__(name)
        # super().set_power(self.start_power * 3)

    def __str__(self):
        return f'Name: {self.name}, HP: {round(self.get_hp())}, M.Atk: {self.start_power * 3}'

    def set_power(self, new_power):
        super().set_power(self.start_power * 3)

    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    def attack(self, target):
        target.take_damage(self.start_power)

    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    def take_damage(self, damage):
        super().take_damage(damage)
        self.set_hp(self.get_hp() - (1.2 * damage))

    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    def heal(self, target):
        target.set_hp(self.get_hp() + self.start_power)

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из
    # действий (атака, исцеление) на выбранную им цель
    def make_a_move(self, friends, enemies):
        min_hp_friend = friends[0]
        if self.get_hp() < 100:
            print(f'{self.name}: Исцеляю себя')
            self.get_hp() + self.start_power
        elif 1 < min_hp_friend.get_hp() < 150:
            for target_heal in friends:
                if target_heal.get_hp() < min_hp_friend.get_hp() and target_heal.get_hp() < 140:
                    min_hp_friend = target_heal
            self.heal(min_hp_friend)
            print(f'{self.name}: Исцеляю {min_hp_friend.name}')
        else:
            min_hp_enemy = enemies[0]
            for target_attack in enemies:
                if target_attack.is_alive():
                    if target_attack.get_hp() < min_hp_enemy.get_hp():
                        min_hp_enemy = target_attack
            self.attack(min_hp_enemy)
            print(f'{self.name}: Атакую {min_hp_enemy.name}')
        super().make_a_move(friends, enemies)

class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    __min_stat_defense = 1

    def __init__(self, name):
        super().__init__(name)
        self.defense = self.__min_stat_defense
        self.shield_status = False


    def __str__(self):
        return f'Name: {self.name}, HP: {round(self.get_hp())}, P.Atk: {self.start_power}, P. def: {self.defense}'

    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)

    def set_power(self, new_power):
        super().set_power(self.start_power / 2)

    def attack(self, target):
        target.take_damage(self.start_power)

    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом
    # отнимается от здоровья
    def take_damage(self, damage):
        super().take_damage(damage)
        self.set_hp(self.get_hp() - (damage / self.defense))

    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает
    # показатель силы в 2 раза.
    def shield_raised(self):
        if not self.shield_status:
            self.shield_status = True
            self.defense *= 2
            self.start_power /= 2

    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает
    # показатель силы в 2 раза.
    def shield_lowered(self):
        if self.shield_status:
            self.shield_status = False
            self.defense /= 2
            self.start_power *= 2

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из
    # действий (атака, поднять щит/опустить щит) на выбранную им цель
    def make_a_move(self, friends, enemies):
        if self.get_hp() >= 120:
            min_hp_enemy = enemies[0]
            for target_attack in enemies:
                if target_attack.is_alive():
                    if target_attack.get_hp() < min_hp_enemy.get_hp():
                        min_hp_enemy = target_attack
            self.attack(min_hp_enemy)
            print(f'{self.name}: Атакую {min_hp_enemy.name}')
        elif self.get_hp() < 95:
            print(f'{self.name}: Щит поднял')
            self.shield_raised()
        else:
            print(f'{self.name}: Щит опустил')
            self.shield_lowered()
        super().make_a_move(friends, enemies)

class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    min_power_multiply = 1

    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = self.min_power_multiply

    def __str__(self):
        return f'Name: {self.name}, HP: {round(self.get_hp())}, ' \
               f'P.Atk: {self.start_power * self.power_multiply}, P.mul: {self.power_multiply}'

    # Методы: - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона
    # (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    def attack(self, target):
        target.take_damage(self.start_power * self.power_multiply)

    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона -
    # damage * ( self.power_multiply / 2)
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage * (self.power_multiply / 2))

    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    def power_up(self):
        self.power_multiply *= 2

    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    def power_down(self):
        self.power_multiply /= 2

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из
    # действий (атака, усиление, ослабление) на выбранную им цель
    def make_a_move(self, friends, enemies):
        if self.power_multiply < 4:
            print(f'{self.name}: Усиливаю атаку')
            self.power_up()
        else:
            min_hp_enemy = enemies[0]
            for target_attack in enemies:
                if target_attack.is_alive():
                    if target_attack.get_hp() < min_hp_enemy.get_hp():
                        min_hp_enemy = target_attack

            self.attack(min_hp_enemy)
            print(f'{self.name}: Атакую {min_hp_enemy.name}')
        super().make_a_move(friends, enemies)
