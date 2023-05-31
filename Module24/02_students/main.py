from Student import Student
import random


def create_list_students(cnt):
    list_students = [Student() for _ in range(cnt)]
    first_names = ('Ivan', 'Alex', 'Oleg', "Roman", 'Maksim', 'Olga', 'Oksana', 'Yana', "Anna", 'Tatyana')
    surnames = ('Kim', 'Minosyan', 'Plug', 'Podoprigora', 'Zabor', 'Ruka', 'Vostok', 'Zapad', 'Svoboda', 'Pobeda')

    for index in range(cnt):
        list_students[index].grade = [random.randint(3, 5) for grade in range(5)]
        list_students[index].group_number = random.randint(1, 3)
        list_students[index].surname_name = random.choice(first_names) + ' ' + random.choice(surnames)

    return list_students


def sort_by_average_grade(stud):
    return sum(stud.grade) / len(stud.grade)


list_students = create_list_students(10)
sorted_list_student = sorted(list_students, key=sort_by_average_grade)

print('Сортировка по возрастанию среднего балла студента')
for index, value in enumerate(sorted_list_student):
    average = sum(sorted_list_student[index].grade) / len(sorted_list_student[index].grade)
    print(f'{sorted_list_student[index].info()}\nСредний балл: {average}\n')

