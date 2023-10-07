class Pet:
    legs = 4
    has_tail = True

    def __str__(self):
        tail = 'да' if self.has_tail else 'нет'
        return 'Всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
            legs=self.legs,
            has_tail=tail
        )


class Cat(Pet):
    def sound(self):
        print('Мяу!')


class Dog(Pet):
    def sound(self):
        print('Гав!')


class Frog(Pet):
    has_tail = False

    def sound(self):
        print('Ква!')
