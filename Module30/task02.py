from typing import List, Dict, Union


def string_to_int(elem: str) -> int:
    return int(elem[4:])


users: List[str] = ['user99', 'user1232', 'user1111', 'user1', 'user1',  'user3', 'user4', 'user5', 'user6']
sorted_users = sorted(users, key=lambda elem: int(elem[4:]))
print(sorted_users)

# Задача 1. Минимум и максимум Мы знаем, что для нахождения минимального и максимального значений в наборе данных
# можно использовать две встроенные функции: min() и max(). И у них тоже можно использовать именованный аргумент key.
# Скажем, дан вот такой список, в котором хранятся результаты соревнований в виде словарей:

# grades: Dict[str, Union[str, int]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41},
# {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
# {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
# {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
# {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
# {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
# {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
# {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
# {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
# ]

# Напишите код, который выводит на экран минимальное и максимальное количество очков из этого списка.
# Используйте только встроенные функции и лямбда-функции, то есть реализуйте решение «в две строки».

grades = [
    {'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24},
    {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
    {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
    {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
    {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
    {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
    {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
    {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
    {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
]
print(f'максимальное ключ-значение: {max(grades, key=lambda x: x["score"])}')
print(f'минимальное ключ-значение: {min(grades, key=lambda x: x["score"])}')

print(f'максимальное значение: {max(grades, key=lambda x: x["score"])['score']}')
print(f'минимальное значение: {min(grades, key=lambda x: x["score"])['score']}')

print('Решение через map')
print(f'список оценок: {list(map(lambda x: x['score'], grades))}')  # для наглядности
print(f'максимальное значение: {max(map(lambda x: x['score'], grades))}')
print(f'минимальное значение: {min(map(lambda x: x['score'], grades))}')


# Задача 2. Сортировка
#
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке: его имя, возраст и остальные данные.
# Вас попросили реализовать для этой базы сортировку по возрасту (по убыванию и по возрастанию).
#
# Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами.
# Затем создайте список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @name.setter
    def name(self, word):
        self._name = word

    def __repr__(self):
        return f"({self.name}, {self.age})"


first = Person("Max", 29)
second = Person("Christine", 21)
third = Person("Anthony", 35)
humans = [first, second, third]
print(humans)
humans.sort(key=lambda x: x.age)
print(humans)
humans.sort(key=lambda x: -x.age)
print(humans)
