class Property:
    """
    Базовый класс, описывающий налог

    Attributes:
        __worth: стоимость имущества
    """
    __worth = 0

    def __init__(self, worth):
        self.__worth = worth

    def get_tax(self):
        """
        Метод возвращает стоимость имущества;
        :return: возвращается стоимость имущества
        """
        return self.__worth

    def set_tax(self):
        """
        Метод расчета налога на имущество;
        :return: self.__worth (int, float): возвращается размер налога на имущество
        """
        pass


class Apartment(Property):
    """
    Класс Квартира, родитель: Property
    """

    def set_tax(self):
        """
        :return возвращается размер налога на недвижимость
        """
        return self.get_tax() * 1e-3


class Car(Property):
    """
    Класс Автомобиль, родитель: Property
    """

    def set_tax(self):
        """
        :return: Возвращается размер налога на автомобиль
        """
        return self.get_tax() * 5e-3


class SummerHouse(Property):
    """
    Класс Дача, родитель: Property
    """
    def set_tax(self):
        """
        :return: Возвращается размер налога на дачу
        """
        return self.get_tax() * 2e-3
