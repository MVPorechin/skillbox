class NameX:
    def __init__(self, name):
        self.name = name


class NameA(NameX):
    def __init__(self, name):
        super().__init__(name)


class NameB(NameX):
    def __init__(self, name):
        super().__init__(name)


class NameC(NameX):
    def __init__(self, name):
        super().__init__(name)


class NameD:
    def __init__(self, name):
        super().__init__(name)


class NameE(NameA, NameB):

    def __init__(self, name):
        super().__init__(name)


class NameF(NameB, NameC):
    def __init__(self, name):
        super().__init__(name)


class NameG(NameB, NameC, NameD):
    def __init__(self, name):
        super().__init__(name)


class NameH(NameC, NameD):
    def __init__(self, name):
        super().__init__(name)


class NameJ(NameE):
    def __init__(self, name):
        super().__init__(name)


class NameK(NameF, NameG, NameH):
    def __init__(self, name):
        super().__init__(name)


class NameZ(NameJ, NameK):
    def __init__(self, name):
        super().__init__(name)


z = NameZ(name='Zapad')

print(z.__class__.__mro__)

#ZJEAKFGBHCDX