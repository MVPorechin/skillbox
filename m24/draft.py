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
    max_speed = '200'
    cur_speed = '0'


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()
car_1.cur_speed = '30'
car_2.cur_speed = '60'
car_3.cur_speed = '90'
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
    headphones_micro = False
    headphones_sensitivity = 100


monitor_1 = Display()
monitor_2 = Display()
monitor_3 = Display()
monitor_4 = Display()
monitor_1.display_freq = 60
monitor_2.display_freq = 144
monitor_3.display_freq = 70
monitor_4.display_freq = 60

headphones_1 = Headphones()
headphones_2 = Headphones()
headphones_3 = Headphones()
headphones_1.headphones_micro = False
headphones_2.headphones_micro = True
headphones_3.headphones_micro = True


