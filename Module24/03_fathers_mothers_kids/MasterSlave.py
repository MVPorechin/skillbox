class Parent:
    def __init__(self, name='Maria', age=32, list_child=['Ivan', 'Olga']):
        self.name = name
        self.age = age
        self.list_child = list_child

    def info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}\n'
              f'Мои дети: {self.list_child}\n')

    def calm_down(self, child):
        if child.name in self.list_child and child.state >= 2:
            print(f'{child.name}, {Child.statuses[child.state]}')
            print(f'{self.name} успокаивает {child.name}')
            child.state -= 1
        else:
            print(f'{child.name} не мой ребенок!')
        print(f'{child.name}, {Child.statuses[child.state]}')

    def feed(self, child):
        if not child.hunger:
            print(f'{self.name} накормил {child.name}')
            child.hunger = True


class Child:
    statuses = {0: 'Спокойный', 1: 'Веселый', 2: 'Грустный', 3: 'Злой'}

    def __init__(self, name='Sergei', age=14, state=2, hunger=1):
        self.name = name
        self.age = age
        self.state = state
        self.hunger = hunger
