from MasterSlave import Parent
from MasterSlave import Child
import random

def make_a_family(cnt_parent, cnt_child):
    lst_parent = [Parent() for _ in range(cnt_parent)]
    lst_child = [Child() for _ in range(cnt_child)]

    first_names = ('Ivan', 'Alex', 'Oleg', "Roman", 'Maksim', 'Olga', 'Oksana', 'Yana', 'Anna', 'Tatyana', 'Ekaterina',
                   'Roman', 'Svyatoslav', 'Nadezhda', 'Elena', 'Valentin', 'Valentina', 'Evgenii', 'Natalya', 'Julia',
                   'Dmitry', 'Vladimir', 'Anatoliy', 'Kapitolina', 'Diana', 'Dariya', 'Oksana', 'Anastasia', 'Alexander',
                   'Vasiliy', 'Nikita', 'Yuriy')

    for index in range(cnt_parent):
        lst_parent[index].name = random.choice(first_names)
        lst_parent[index].age = random.randint(32, 42)
        lst_parent[index].list_child = [random.choice(first_names) for _ in range(random.randint(4, 8))]

    for index in range(cnt_child):
        lst_child[index].name = random.choice(first_names)
        lst_child[index].age = random.randint(1, 16)
        lst_child[index].state = random.randint(0, 3)
        lst_child[index].hunger = random.randint(0, 1)

    return show(lst_parent, lst_child)


def show(parents, children):
    return [(parent.calm_down(child), parent.feed(child)) for parent in parents for child in children]


make_a_family(5, 10)


