#9.1 Модуль os: генерация путей и метод listdir
import os

folder_name = 'project'
file_name = 'my_file.txt'
path = 'docs/{folder}/{file}'.format(
    folder=folder_name,
    file=file_name,
)

# print(path)

real_path = os.path.join('docs', folder_name, file_name)
print(real_path)
abs_path = os.path.abspath(file_name)
print(abs_path)
os.path.abspath('new_folder')
os.path.abspath(os.path.join('..', 'new_folder'))
os.path.abspath(os.path.join('/new_folder'))
os.path.abspath(os.path.join(os.path.sep, 'new_folder'))


def print_dirs(project):
    print(f'\nСодержимое директории {project}')
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print(f'       {path}')


projects_list = ['pet_project', 'aqua_disco_project']

for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join(i_project))
    print_dirs(path_to_project)