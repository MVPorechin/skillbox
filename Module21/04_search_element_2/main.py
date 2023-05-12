def find_key(struct, key, user_input_depth):
    if user_input_depth != -1:
        if key in struct:
            return struct[key]

        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, user_input_depth - 1)
                if result:
                    break
        else:
            result = None

        return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок2',
            'body2': {
                'h3': 'Здесь будет мой заголовок3',
                'div2': 'Тут, наверное, какой-то блок2',
                'body3': {
                    'h4': 'Здесь будет мой заголовок4',
                    'body4': {
                        'h4': 'Здесь будет мой заголовок4',
                        'div3': 'Тут, наверное, какой-то блок3',
                        'p4': 'А вот здесь новый абзац4'
                    },
                    'div4': 'Тут, наверное, какой-то блок4',
                    'p3': 'А вот здесь новый абзац3'
                },
                'p1': 'А вот здесь новый абзац1'
            },
            'div': 'Тут, наверное, какой-то блок',
            'p2': 'А вот здесь новый абзац2'
        }
    }
}


user_key = input('Введите искомый ключ: ')
ask_max_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if ask_max_depth == 'y':
    input_max_depth = int(input('Введите максимальную глубину: '))
    value = find_key(site, user_key, input_max_depth)
else:
    value = find_key(site, user_key, 65536)

print(f'Значение ключа: {value}')

# зачет!
