def min_len_elem(*args):
    return len(sorted(args, key=len)[0])


def compress(*args):
    list_of_args = [tuple(value)[index] for index in range(min_len_elem(args)) for value in args]
    result = []
    for i_index in range(0, len(list_of_args), len(args)):
        out_tuple = ()
        for j_index in range(i_index, i_index + len(args)):
            out_tuple += (list_of_args[j_index],)
        result.append(out_tuple)
    return result


a = [1, 2, 3, 4, 5]
b = {1: "s", 2: "q", 3: 4}
x = (1, 2, 3, 4, 5)
print(compress(a, b, x))

# зачет!
