def recursive_sum(*args):
    result = 0
    if len(args) == 1:
        for lst in args[0]:
            if isinstance(lst, list):
                result += recursive_sum(lst)
            else:
                result += lst
    else:
        for num in args:
            result += num
    return result


# result = recursive_sum([[1, 2, [3]], [1], 3])
output = recursive_sum(1, 2, 3, 4, 5)
print(f'Ответ в консоли: {output}')


# зачет!
