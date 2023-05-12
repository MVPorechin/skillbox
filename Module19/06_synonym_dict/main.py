number_pair_word = int(input('Введите количество пар слов: '))
synonym_dict = dict()

for num in range(1, number_pair_word + 1):
    text = input(f'{num} пара: ').lower().split(' - ')
    list_text = list(text)
    synonym_dict[list_text[0]] = list_text[1]


search = True
while search:
    find_syn = False
    search_word = input('Введите слово: ').lower()
    for key, value in synonym_dict.items():
        if value == search_word:
            find_syn = True
            print(f'Синоним: {key}')

    if not find_syn:
        print('Такого слова в словаре нет.')

# зачет!
