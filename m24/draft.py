class User:
    user_name = 'Admin'
    password = 'querty'
    is_banned = False


user_1 = User() #экземлпяр класса User

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
