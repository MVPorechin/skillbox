class Person:
    """ Базовый класс Человек
    Args:
        name (str): имя
        age(int): возраст

    Attributes:
        _name(str) : имя
        _age(int) :возраст ( от  1 до 100 лет, иначе ошибка)
    """
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> None:
        return f'Имя: {self._name}, Возраст: {self._age}'

    @property
    def age(self) -> int:
        """
        Геттер, Возращает возраст
        """
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """
        Сеттер.
        Устанавливает возраст в диапазоне от 1 до 100,
        иначе вызывает исключение
        """
        if age in range(1, 100):
            self._age = age
        else:
            raise Exception('Недопустимый аргумент')

    @property
    def name(self) -> str:
        """
        Геттер, Возращает имя
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Сеттер.
        Устанавливает имя
        """
        self._name = name


maxim = Person(name='Maxim', age=23)
print(maxim)
print(maxim.age)
maxim.age = 32
print(maxim.age)
print(maxim)