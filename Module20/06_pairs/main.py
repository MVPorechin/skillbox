import random
original_list = [random.randint(0, 10) for number in range(10)]


def list_to_matrix(input_list):
    list_tuple = []
    for index in input_list:
        if len(input_list) != 0:
            list_tuple.append(tuple(input_list[:2]))
            input_list = input_list[2:]
    return list_tuple


print(f'Оригинальный список: {original_list}\nНовый список: {list_to_matrix(original_list)}')

# зачет!
