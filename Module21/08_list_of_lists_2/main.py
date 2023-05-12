def unpack_list(input_list):
    output_list = []
    for value in input_list:
        if isinstance(value, list):
            output_list += unpack_list(value)
        else:
            output_list.append(value)
    return output_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

output = unpack_list(nice_list)
print(f'Ответ: {output}')

# зачет!
