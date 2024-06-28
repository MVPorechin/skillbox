import math


class MyMath:
    """
    Класс для математических вычислений, связанных с фигурами.
    """

    @classmethod
    def circle_len(cls, radius: int) -> float:
        """
        Метод вычисление длины окружности
        :param radius: на вход подаем радиус

        """
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        """
        Метод вычисление площади окружности
        :param radius: на вход подаем радиус

        """
        return math.pi * pow(radius, 2)

    @classmethod
    def volume_sq(cls, length_edge: int) -> float:
        """
        Метод вычисление объёма куба
        :param length_edge: на вход подаем длину стороны куба

        """
        return pow(length_edge, 3)

    @classmethod
    def surface_area_sphere(cls, radius: int) -> float:
        """
        Метод вычисление площади поверхности сферы
        :param radius: на вход подаем радиус

        """
        return math.pi * 4 * pow(radius, 2)