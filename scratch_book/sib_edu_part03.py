class Car:
    """
    Класс описывающий автомобиль
    Attributes:
        name(str): имя автомобиля
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        print('')
        return self.name


my_car = Car(name='cuser_L200')
print(my_car)


