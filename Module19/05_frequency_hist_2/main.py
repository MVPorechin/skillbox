def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


def invert_historgram(number, hist):
    invert_hist = dict()
    for index in range(1, number + 1):
        invert_hist[index] = [key for key, value in hist.items() if value == index]

    return invert_hist


text = input('Введите текст: ').lower()
hist = histogram(text)
invert_h = invert_historgram(3, histogram(text))
for index_sym in sorted(hist.keys()):
    print(f'{index_sym} : {hist[index_sym]}')

print(f'\nИнвертированный словарь частот:')
for index_key, index_value in invert_h.items():
    print(f'{index_key} : {index_value}')

# зачет!
