# Задача 1. Координаты точки В одной из практик предыдущего модуля была задача на реализацию класса «Точка».
# Модернизируйте класс по следующему условию: объект «Точка» на плоскости имеет координаты x и y; при создании новой
# точки могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.

# Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
#
# Предоставление информации о точке (используйте магический метод str).
# Геттер и сеттер для x.
# Геттер и сеттер для y.
# Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.


class Dot:

    def __init__(self, ord_x=0, ord_y=0):
        self.__ord_x = ord_x
        self.__ord_y = ord_y

    def __str__(self):
        return "Точка с координатами X: {}\tY: {}".format(self.__ord_x, self.__ord_y)

    def get_coordinate_x(self):
        return self.__ord_x

    def get_coordinate_y(self):
        return self.__ord_y

    def check_value(self, value):
        if isinstance(value, str) and value.isdigit():
            value = float(value)
        if isinstance(value, (int, float)):
            return value
        else:
            raise TypeError('Значение должно быть числом')

    def set_x(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__ord_x = checker_value

    def set_y(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__ord_y = checker_value


new_dot = Dot(-1, 1)
print(new_dot)
print(new_dot.get_coordinate_x(), new_dot.get_coordinate_y())
new_dot.set_x(10)
new_dot.set_y(-10)
print(new_dot.get_coordinate_x(), new_dot.get_coordinate_y())
print(new_dot)


# Задача 2. Человек
#
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв)
# и возрастом (должен быть в диапазоне от 0 до 100),
# а внутри класса считается общее количество инициализированных объектов.
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
# а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
#
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# сеттером и «крайне не рекомендуемым», который был показан в видео.

class Human:
    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)

        Human.__count += 1

    def __str__(self):
        return f"Имя: {self.__name}\tВозраст: {self.__age} лет"

    def set_name(self, value):
        if isinstance(value, str) and value.isalpha():
            self.__name = value
        else:
            raise ValueError('Ошибка в имени')

    def set_age(self, value):
        if isinstance(value, (int, float)) and 0 <= value <= 100:
            self.__age = value
        else:
            raise ValueError('Ошибка в возрасте')

    def get_count(self):
        return self.__count

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


anna = Human('Анна', 19)  # значения передадутся в сеттер
ruzanna = Human('Рузанна', 18)  # значения передадутся в сеттер
print(anna.get_count())
print(anna, '\n', ruzanna)
anna.set_age(21)
print(anna, '\n', ruzanna)
anna.set_name('Сюзанна')
print(anna, '\n', ruzanna)

anna._Human__age = 99 # «крайне не рекомендуемый» метод
print(anna)