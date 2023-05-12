import random


def sort_tuple(input_tuple):
    tuple_float = (isinstance(index, float) for index in input_tuple)
    if True in tuple_float:
        return input_tuple
    else:
        return sorted(list(input_tuple))


# rand_tuple = (random.randint(-10, 10) for number in range(10))
# rand_tuple = (-4, 3, -6, 3, -2, -6.3, -1, 0, 10, -7)
# rand_tuple = (round(random.uniform(-10, 10), 2) for number in range(10))
# print(f'{sort_tuple(rand_tuple)}')

# зачет!
