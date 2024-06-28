import os


def count_all_line_in_files(path_to_folder=None):
    count_all_line = 0
    for obj in os.listdir(path_to_folder):
        with open(os.path.join(path_to_folder, obj), encoding='UTF-8') as file:
            count_all_line += sum(1 for _ in file)
    yield count_all_line


path = 'D:\\python\\Python_Basic\\Module25\\04_RPG_game'
for item in count_all_line_in_files(path_to_folder=path):
    print(item)

# зачет!
