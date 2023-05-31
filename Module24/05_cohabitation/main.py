from Sims import Human
from Sims import House
from Sims import Locker
from Sims import Fridge
import random

day = 1
Olya = Human('Ольга', 50, 'ул.Краснознаменская, д.17')
Anton = Human('Антон', 50, 'ул.Краснознаменская, д.17')
list_residents = [Olya, Anton]
my_house = House('ул.Краснознаменская, д.17')
my_fridge = Fridge()
drawer = Locker()
drawer.get_locker(Olya.house)
my_fridge.get_fridge(Olya.house)

while day <= 365:
    print(f'Наступает {day} день')
    for resident in list_residents:
        if resident.satiety < 20:
            print(f'{resident.name} проголодался, кушаем')
            resident.to_eat(my_fridge)
        elif my_fridge.meal < 10:
            print(f'В холодильнике заканчивается еда {resident.name} идет в магазин')
            resident.go_to_store_for_food(my_fridge, drawer)
        elif drawer.money < 50:
            print(f'Деньги заканчиваются {resident.name} идет на работу')
            resident.work(drawer)
        elif random.randint(1, 6) == 1:
            print(f'{resident.name} идет на работу')
            resident.work(drawer)
        elif random.randint(1, 6) == 2:
            print(f'{resident.name} идет кушать')
            resident.to_eat(my_fridge)
        else:
            print(f'{resident.name} играет в игры')
            resident.play_games()
        if resident.satiety == 0:
            resident.condition = False
        if not resident.condition:
            print(f'{resident.name} умер от голода')
            break
    print(f'День {day} закончился, денег {drawer.money} и еды {my_fridge.meal} осталось')
    day += 1
