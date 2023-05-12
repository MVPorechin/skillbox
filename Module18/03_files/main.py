name_file = input('Название файла:')

result = '{new_file}'.format(
    new_file=name_file
)

if not result.endswith('.txt'):
    print('Ошибка: не верное расширение файла')
elif not result.startswith('example'):
    print('Ошибка: неверно имя файла')
else:
    print('Файл назван верно')

# зачет!
