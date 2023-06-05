class Person:
    """
    Базовый класс, описывающий человека

    __count: общее количество
    Args:
        name (str): передается имя человека
        age (int): передается возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов
    """
    __count = 0
    max_count = 5

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        self.__location = 'Moscow'
        if Person.__count > self.max_count:
            raise Exception('Слишком много людей')
        Person.__count += 1

    def get_age(self):
        """
        Геттер для получения возраста
        :return: __age
        :rtype: int
        """
        return self.__age

    def set_age(self, age):  # сеттер
        """
        Сеттер для установления возраста
        :param age: возраст
        :type age: int
        :raise Exception: если возраст не в границах от 1 до 90, то вызывается исключение
        """
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')

    def __str__(self):
        return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)

    def get_count(self):  # геттер
        return self.__count

    def get_name(self):
        return self.__name


class Student(Person):
    """
    Класс Работник. Родитель: Person
    Args:
        name (str): передается имя человека
        age (int): передается возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов
        job (str): должность работника
    """
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.unisersity = university

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                "Студент учится в университете {}".format(self.unisersity)
            )
        )
        return info


class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                "Компания: {}\tЗарплата: {}".format(self.company, self.salary)
            )
        )
        return info


print(Person.__doc__)