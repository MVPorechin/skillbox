import random


def slicer(input_tuple, random_number):
    list_input_tuple = list(set(input_tuple))
    if random_number == 0 or None:
        tuple()
    elif input_tuple.count(random_number) > 1:
        return (random_number for index in range(len(list_input_tuple)))
    else:
        list_input_tuple[0], list_input_tuple[-1] = random_number, random_number
        return tuple(list_input_tuple)


random_value = random.randint(0, 10)
tuple_input = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
print(slicer(tuple_input, random_value))

# зачет!
