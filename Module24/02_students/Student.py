import random

class Student:
    def __init__(self, surname_name='Ivan Petrov', group_number=1, grade=[3, 3, 3, 3, 3]):
        self.surname_name = surname_name
        self.group_number = group_number
        self.grade = grade

    def info(self):
        print(f'ФИ: {self.surname_name}\n'
              f'Номер группы: {self.group_number}\n'
              f'Успеваемость: {self.grade}\n')
