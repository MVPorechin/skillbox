class Potapo:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} в стадии {Potapo.states[self.state]}')


class PotapoGarden:
    def __init__(self, count):
        self.potatoes = [Potapo(index) for index in range(1, count + 1)]

    def grow_all(self):
        print(f'картошка прорастает!')
        for i_potapo in self.potatoes:
            i_potapo.grow()

    def are_all_ripe(self):
        if not all([i_potapo.is_ripe() for i_potapo in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела! можно собирать\n')
