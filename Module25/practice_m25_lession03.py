class Pet:
    legs = 4
    has_tail = True

    def __init__(self):
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


cat = Cat()
dog = Dog()
print(cat)
print(dog)
cat.sound()
dog.sound()