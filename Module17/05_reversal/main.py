def reverse(text):
    index_h = [index for index, word in enumerate(text) if word == 'h']
    if len(index_h) == 2:
        result = text[index_h[0] + 1:index_h[-1]]
    else:
        result = text[index_h[1]:index_h[-1]]
    reverse = result[::-1]
    return reverse


text = input('Введите строку: ')
print(f'Развёрнутая последовательность между первым и последним h: {reverse(text)}')

# зачет!
