class Hero():
    def __init__(self, name: str, health: int, power: int):
        self.name = name
        self.health = health
        self.power = power

    def __str__(self):
        return f'\nГерой {self.name}, ' \
               f'Здоровье {self.health}, '\
               f'Сила {self.power}'

    def strike(self, enemy: object):
        """
        Метод атака
        :param enemy:
        :return:
        """
        print(f'{self.name} атакует {enemy.name} c силой {self.power}')
        enemy.health = enemy.health - self.power
        print(f'{enemy.name} получил урон {self.power}, '
              f'жизненной силы осталось {enemy.health}')


class DragonClass(Hero):
    """
    Класс-примесь для класса Hero, родитель Hero
     """
    def strike(self, enemy: object):
        """
        Метод описывающий атаку, увеличенную на 2
        :param enemy:
        :return:
        """
        enemy.health = enemy.health - (self.power * 2)


knight = Hero(name='Владимир', health=500, power=50)
dragon = DragonClass(name='Дракон', health=50, power=99)
lizard = DragonClass(name='Ящер', health=80, power=66)

enemies = [dragon, lizard]
play = True
while play:
    for npc in enemies:
        npc.strike(enemy=knight)
        knight.strike(enemy=npc)
        if npc.health <= 0:
            print(f'{knight.name} разбил {npc.name}')
            enemies.remove(npc)
    print(knight, dragon, lizard)
    if len(enemies) == 0 and knight.health > 0:
        print(f'Герой {knight.name} одержал победу!')
        play = False
    elif knight.health < 0:
        print(f'Герой {knight.name} разбит!')
        play = False


