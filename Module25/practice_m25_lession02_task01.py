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
# и возрастом (должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов.
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
# а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
#
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# сеттером и «крайне не рекомендуемым», который был показан в видео.

