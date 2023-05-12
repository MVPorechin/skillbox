def count_and_add_symbol(text):
    decrypt = []
    count = 1
    for index in range(len(text) - 1):
        if text[index] == text[index + 1]:
            count += 1
        else:
            decrypt.append(text[index] + str(count))
            count = 1
        decrypt_str = ''.join(decrypt)
    return print(f'Закодированная строка: {decrypt_str}')


input_str = list(input('Введите строку: '))
input_str += " "
# input_str = 'aaAAbbсaaaA'
count_and_add_symbol(input_str)

# зачет!
