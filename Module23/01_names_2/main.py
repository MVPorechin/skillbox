import os


def names(file_name):
    with open(file_name, 'r', encoding='utf8') as peoples, open('errors.log', 'w', encoding='utf8') as log_file:
        result = 0
        list_position = list()

        for position, line in enumerate(peoples, 0):
            try:
                clear_line_len = len(line.rstrip())
                if clear_line_len == 2:
                    list_position.append(position)
                    raise Exception(f'Ошибка в строке {position}')
                else:
                    result += clear_line_len
            except Exception as exc:
                log_file.write(str(type(exc)) + ' менее трёх символов в строке: ' + str(position))

    return list_position, result


path_to_file = os.path.abspath('people.txt')
error_position, summ_sym_in_file = names(path_to_file)
print(f'Ошибка: менее трёх символов в строке: {error_position}\nОбщее количество символов: {summ_sym_in_file}.')

# зачет!
