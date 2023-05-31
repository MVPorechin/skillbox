import random


class PersonAttributes:

    def __init__(self, name, health=100, physical_attack=20):
        self.name = name
        self.health = health
        self.physical_attack = physical_attack
        self.status = True

    def attack(self, enemy):
        if enemy.health > 0 and self.health > 0:
            chance = random.randint(0, 1)
            if chance:
                enemy.health -= self.physical_attack
                print(f'{self.name} атаковал {enemy.name}\n{enemy.name} состояние здоровья {enemy.health}')
            else:
                print(f'{self.name} промазал')
        elif enemy.health == 0:
            enemy.status = False
        else:
            self.status = False
            print(f'{enemy.name} Одержал победу!')


class Fight:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    def round(self):
        while self.first_player.status and self.second_player.status:
            if self.first_player.status:
                self.first_player.attack(self.second_player)
            if self.second_player.status:
                self.second_player.attack(self.first_player)
