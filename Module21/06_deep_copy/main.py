import copy


def find_value(n_site, name_prod):
    replace_value = ['телефон', 'iphone']
    for key, item in n_site.items():
        if replace_value[0] in item:
            new_item = item.replace(replace_value[0], name_prod)
            n_site[key] = new_item
        elif replace_value[1] in item:
            new_item = item.replace(replace_value[1], name_prod)
            n_site[key] = new_item
        if isinstance(item, dict):
            find_value(item, name_prod)
    return n_site


def output_new_site(cnt, original_site):
    for _ in range(cnt):
        new_site = copy.deepcopy(original_site)
        name_product = input('Введите название продукта для нового сайта: ')
        print(f'Сайт для {name_product}')
        print(find_value(new_site, name_product))


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

count = int(input('Сколько сайтов: '))
output_new_site(count, site)

# зачет!
