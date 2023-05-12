import os


def count_and_summ(path, list_result):
    for i_elem in os.listdir(path):
        path = os.path.join(path, i_elem)
        if os.path.isdir(path):
            list_result[0] += 1
            count_and_summ(path, list_result)
        if os.path.isfile(path):
            list_result[1] += 1
            list_result[2] += os.path.getsize(path)
    return list_result


result_list = [0, 0, 0]
path_to_folder = os.path.abspath(os.path.join('..', '..', 'Module21'))
result_folder_files_size = count_and_summ(path_to_folder, result_list)

print(f'{path_to_folder}'
      f'\nРазмер каталога (в Кб): {result_folder_files_size[2] / 1024}'
      f'\nКоличество подкаталогов: {result_folder_files_size[0] - 1}'
      f'\nКоличество файлов: {result_folder_files_size[1]}')

# зачет!
