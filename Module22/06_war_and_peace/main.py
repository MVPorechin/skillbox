import os
import zipfile


def count_sym_in_text(string_from_file):
    ignore_symbol = ['–', '*', '&', '=', ')', '(', ';', '“', '…', '/', '°', '„', '`', '', ' ', '\n', '-', '"', '<', '>',
                     '№', '!', '?', ',', '.', ':', '«', '[', ']', '}', '{', '—', '\xa0', "'", '»']

    return {sym: string_from_file.__count(sym) for sym in set(string_from_file) if sym not in ignore_symbol}


def count_all_sym_in_text(path):
    dict_count_freq = {}
    first_run = True
    for line in open(path, 'r', encoding='utf-8'):
        if first_run:
            dict_freq_sym_all = count_sym_in_text(line)
            first_run = False
        dict_count_freq.update(count_sym_in_text(line))
        dict_freq_sym_all = {key: dict_freq_sym_all.get(key, 0) + dict_count_freq.get(key, 0)
                             for key in set(dict_freq_sym_all) | set(dict_count_freq)}

    sorted_by_value = {key: value for key, value in
                       sorted((dict_freq_sym_all.items()), key=lambda item: item[1], reverse=True)}

    sorted_by_alphabet = open('sort_sym_in_text.txt', 'w', encoding='utf-8')
    path_to_sorted_file = os.path.abspath(os.path.join('sort_sym_in_text.txt'))
    write_to_file = {sorted_by_alphabet.write(str(key) + ' ' + str(value) + '\n') for key, value in
                     sorted_by_value.items()}

    sorted_by_alphabet.close()

    return [print(line) for line in open(path_to_sorted_file, 'r', encoding='utf-8')]


path_to_archive = os.path.abspath(os.path.join('voyna-i-mir.zip'))
with zipfile.ZipFile(path_to_archive, 'r') as zip_file:
    zip_file.extractall(os.path.curdir)

path_to_file = os.path.abspath(os.path.join('voyna-i-mir.txt'))
count_all_sym_in_text(path_to_file)

# зачет!
