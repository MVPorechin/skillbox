import random

class User:
    user_name = 'Admin'
    password = 'querty'
    is_banned = False


user_1 = User()  # экземлпяр класса User

# user_1.user_name = 'Tom'
# print(user_1.user_name)
# user_2 = User()
# print(user_2.user_name)
user_2 = User()
user_2.user_name = 'Tom'
print(user_1.user_name, user_2.user_name)
User.user_name = 'noname'
print(user_1.user_name, user_2.user_name)


# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
class Toyota:
    color_auto = 'Red'
    price = '1000000'
    max_speed = 200
    cur_speed = 0


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()
car_1.cur_speed = random.randint(0, 200)
car_2.cur_speed = random.randint(0, 200)
car_3.cur_speed = random.randint(0, 200)
print(car_1.cur_speed, car_2.cur_speed, car_3.cur_speed)

# Задача 2. Однотипные объекты В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора
# есть четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана. Все четыре
# монитора отличаются только частотой.
#
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в
# наличии микрофона.


class Display:
    display_name = 'AOC'
    display_matrix = 'IPS'
    display_res = '4k'
    display_freq = 144


class Headphones:
    headphones_name = 'Marshall'
    headphones_micro = True
    headphones_sensitivity = 108


monitors = [Display() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]
for index, number in enumerate([60, 144, 70, 50]):
    monitors[index].display_freq = number

headphones[0].headphones_micro = False


