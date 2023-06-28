from collections.abc import Iterable


class Person:
    def __init__(self, name: str, age: int, friends: list) -> None:
        self.__name = name
        self.__age = age
        self.__friends = friends

    def __str__(self):
        return  "Имя: {}\tВозраст: {}\tДрузья: {}".format(
            self.__name, self.__age, self.__friends
        )

    def set_age(self,age) -> None:
        self.__age = age

    def get_age(self) -> int:
        return self.__age


def fibonacci(number: int) -> Iterable[int]:
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
        if cur_val > 10 ** 6:
            return
