# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
#
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).

class Unit:
    def __init__(self, hp):
        self.__hp = hp

    def set_hp(self, amount):
        self.__hp = amount

    def get_hp(self):
        return self.__hp

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - 0)


class Soldier(Unit):

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount)


class Citizen(Unit):

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount * 2)


guard = Soldier(hp=100)
man = Citizen(hp=99)
guard.set_hp(amount=100)
man.set_hp(amount=90)
print(guard.get_hp(), man.get_hp())

guard.get_damage(amount=10)
man.get_damage(amount=11)
print(guard.get_hp(), man.get_hp())

# Задача 2. Полёт
#
# Иногда для реализации дочерних классов используется так называемый класс-роль,
# где также описываются общие атрибуты и методы, но в программе инициализируются объекты только дочерних классов,
# а базовый класс-роль не трогается. К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться.
#
#
#
# Реализуйте класс «Может летать».
#
# Атрибуты:
#
# Высота = 0.
# Скорость = 0.
# Методы:
#
# Взлететь (в теле прописать pass).
# Лететь (в теле прописать pass).
# Приземлиться (установить высоту и скорость в значение 0).
# Вывести высоту и скорость на экран.
#
#
# Затем реализуйте два дочерних класса:
#
# «Бабочка», который может:
#
# Взлететь (высота = 1).
# Лететь (скорость = 0.5).

# «Ракета», которая может:
#
# Взлететь (высота = 500, скорость = 1000).
# Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).


class CanFly:
    def __init__(self):
        self.altitude = 0
        self.velocity = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return "{} высота {} скорость {}".format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.1


class Aircraft(CanFly):

    def take_off(self):
        self.velocity = 300
        self.velocity = 1000

    def fly(self):
        self.velocity = 800


class Missile(CanFly):

    def take_off(self):
        self.velocity = 1000
        self.altitude = 10000

    def land_on(self):
        self.altitude = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print("Ракета показала себя великолепно. Только упала не на ту планету (С) Вернер фон Браун")


fly = Butterfly()
superjet = Aircraft()
dagger = Missile()

dagger.land_on()