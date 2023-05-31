class Water:
    def __init__(self, name='Вода'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Snow):
            return Ice()
        elif isinstance(other, Water):
            return Whirlwind()
        elif isinstance(other, Cold):
            return Ice()
        elif isinstance(other, EarthQuake):
            return Tsunami()
        else:
            return None


class Wind:
    def __init__(self, name='Воздух'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Snow):
            return SnowStorm()
        elif isinstance(other, Wind):
            return Tornado()
        elif isinstance(other, Wind):
            return Tornado()
        else:
            None


class Fire:
    def __init__(self, name='Огонь'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Wind):
            return FireStorm()
        elif isinstance(other, Ice):
            return Water()
        elif isinstance(other, Gas):
            return Explosion()
        else:
            None


class Earth:
    def __init__(self, name='Земля'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Snow):
            return Avalanche()
        elif isinstance(other, Earth):
            return EarthQuake()
        else:
            None


class Snow:
    def __init__(self, name='Снег'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Wind):
            return SnowStorm()
        else:
            None


class Tornado:
    def __init__(self, name='Торнадо'):
        self.name = name


class Storm:
    def __init__(self, name='Шторм'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, EarthQuake):
            return Tsunami()
        else:
            None


class Explosion:
    def __init__(self, name='Взрыв'):
        self.name = name


class Gas:
    def __init__(self, name='Газ'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Wind):
            return AttackOfDeadMen()
        else:
            None


class Cold:
    def __init__(self, name='Холод'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Water):
            return Ice()
        else:
            None


class Whirlwind:
    def __init__(self, name='Буря'):
        self.name = name


class AttackOfDeadMen:
    def __init__(self, name='Атака мертвецов'):
        self.name = name


class Tsunami:
    def __init__(self, name='Цунами'):
        self.name = name


class EarthQuake:
    def __init__(self, name='Землетрясение'):
        self.name = name


class Ice:
    def __init__(self, name='Лед'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Wind):
            return IceBlizzard()
        else:
            None


class IceBlizzard:
    def __init__(self, name='Ледяной шторм'):
        self.name = name


class SnowStorm:
    def __init__(self, name='Буран'):
        self.name = name


class LandSlide:
    def __init__(self, name='Оползень'):
        self.name = name


class Avalanche:
    def __init__(self, name='Лавина'):
        self.name = name


class Dust:
    def __init__(self, name='Пыль'):
        self.name = name


class FireStorm:
    def __init__(self, name='Огненный'):
        self.name = name


class Lava:
    def __init__(self, name='Лава'):
        self.name = name


class Dirt:
    def __init__(self, name='Грязь'):
        self.name = name


class Steam:
    def __init__(self, name='Шторм'):
        self.name = name
