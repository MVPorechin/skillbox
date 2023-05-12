import os
from typing import List, Any


def file_to_strip_list(path):
    for line in open(path, 'r'):
        strip_line = list(line.lower())
    result = {sym: strip_line.count(sym) for sym in strip_line if sym not in [' ', '.']}

    return sort_and_procent(result)


def sort_and_procent(lst_file):
    sorted_by_values = {key: value for key, value in sorted(lst_file.items(), key=lambda item: item[1], reverse=True)}
    sorted_by_keys = {key: value for key, value in sorted(sorted_by_values.items())}
    sorted_dict = {key: value for key, value in sorted(sorted_by_keys.items(), key=lambda item: item[1], reverse=True)}
    result = {key: round(value / sum(sorted_dict.values()), 3) for key, value in sorted_dict.items()}

    return write_and_output_to_file(result)


def write_and_output_to_file(sorted_dict):
    output_file = open('analysis.txt', 'w')
    write_to_file = [output_file.write(str(key) + ' ' + str(value) + '\n')
                     for key, value in sorted_dict.items()]

    output_file.close()
    path_to_analysis_file = os.path.abspath(os.path.join('analysis.txt'))

    return [print(line) for line in open(path_to_analysis_file, 'r')]


path_to_file = os.path.abspath(os.path.join('text.txt'))
list_file = file_to_strip_list(path_to_file)

# зачет!
