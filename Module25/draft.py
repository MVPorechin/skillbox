class Vapor:
    def __str__(self):
        return "Пар"

    pass


class Dirt:
    def __str__(self):
        return "Грязь"


class Water:
    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            None


class Air:
    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()

    pass


class Fire:
    def __str__(self):
        return "Огонь"

    pass


class Earth:
    def __str__(self):
        return "Земля"

    pass


class Storm:

    def __str__(self):
        return 'Шторм'

    pass


water = Water()
air = Air()
fire = Fire()
earth = Earth()
print(air + water, water + fire, water + earth)
