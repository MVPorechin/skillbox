def zip_function(*args):
    return range(len(sorted(args, key=len)[0]))


def compress(v_string, v_tuple):
    output_compress = ((v_string[index], v_tuple[index]) for index in zip_function(v_string, v_tuple))
    return [print(f'{value}') for value in output_compress]


input_string = 'abcd'
input_tuple = (10, 20, 30, 40)

compress(input_string, input_tuple)

# зачет!
