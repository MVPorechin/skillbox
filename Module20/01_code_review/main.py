students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def list_pair_students():
    pair_list = [(key, value['age']) for key, value in students.items()]
    return pair_list


def list_hobby_all_students():
    list_hobby = {value for index in range(1, 4) for value in students[index]['interests']}
    return list_hobby


def len_all_surname_students():
    len_all_surname = [len(value['surname']) for key, value in students.items()]
    return sum(len_all_surname)


print(f'Список пар "ID студента — возраст": {list_pair_students()}')
print(f'Полный список интересов всех студентов: {list_hobby_all_students()}')
print(f'Общая длина всех фамилий студентов: {len_all_surname_students()}')

# зачет!
