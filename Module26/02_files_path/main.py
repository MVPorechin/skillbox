import os

my_path = 'd:\\backup'
from_root_disk = os.path.abspath(os.sep)
get_disk_word = os.path.abspath('.').split(os.path.sep)[0]


def gen_files_path(folder=os.path.abspath(os.sep), search_element=None) -> str:
    for current_path, dirs_name, files_name in os.walk(folder):
        if search_element in dirs_name:
            yield os.path.join(current_path, search_element)
            break
        yield os.path.join(current_path, search_element)


for file in gen_files_path(folder='c:\\', search_element='System32'):
    print(file)

# зачет!
