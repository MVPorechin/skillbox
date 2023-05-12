import os


def found_and_resolve(path):
    first_tour_file = open(path, 'r')
    second_tour_file = open('second_tour.txt', 'w')
    second_tour_file.write('2\n')
    list_4_sorted = list()
    print(f'Содержимое файла {path}')
    for line in first_tour_file:
        print(line)
        if len(line) <= 3:
            limit = int(line)
        else:
            list_line = line.split()
            list_line[1] = list_line[1][:1] + '.'
            list_line[0], list_line[1] = list_line[1], list_line[0]
            if int(list_line[2]) > limit:
                list_4_sorted.append(list_line)

    sorted_list = sorted(list_4_sorted, key=lambda age: age[2], reverse=True)
    output_result_to_file = [second_tour_file.write(str(index_sl) + ') ' + ' '.join(value_sl) + '\n')
                             for index_sl, value_sl in enumerate(sorted_list, 1)]

    first_tour_file.close()
    second_tour_file.close()

    return output_result(os.path.abspath(os.path.join('second_tour.txt')))


def output_result(path_to_file):
    second_tour_file = open(path_to_file, 'r')
    print(f'Содержимое файла {path_to_file}:')

    return [print(value_stf) for value_stf in second_tour_file]


first_file_path = os.path.abspath(os.path.join('first_tour.txt'))
found_and_resolve(first_file_path)

# зачет!
