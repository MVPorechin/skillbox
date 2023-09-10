from typing import List


class Person:
    """ Базовый класс Человек"""
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age


class Employee(Person):
    """ Работник. Дочерний класс от Person """
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__salary = 20000

    def get_salary(self) -> int:
        return self.__salary


class Parent(Person):
    """ Родитель. Дочерний класс от Person """
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__kids = ['Tom', 'Kate']

    def get_kids(self) -> List[str]:
        return self.__kids


class Citizen(Parent, Employee):
    """ Житель - является и Родителем и Работником """
    pass


my_citizen = Citizen(name='Maxim', age=34)
print(my_citizen.__class__.__mro__)
