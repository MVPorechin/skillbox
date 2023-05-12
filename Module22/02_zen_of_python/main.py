import os


def find_step_4_reverse(path):
    find_position_regex_sym = 0
    tab = 0
    step = list()
    for position in open(path, 'r'):
        step.append(find_position_regex_sym + tab)
        find_position_regex_sym += len(position)
        tab += 1

    return output_file(step[::-1], path)


def output_file(rev_step, path):

    file_txt = open(path, 'r')
    for _ in range(len(rev_step)):
        file_txt.seek(rev_step[_])
        print(f'{file_txt.readline()}')
    file_txt.close()


path_to_file = os.path.abspath(os.path.join('zen.txt'))
find_step_4_reverse(path_to_file)

# зачет!
