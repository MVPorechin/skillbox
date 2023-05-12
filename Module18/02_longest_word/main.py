input_str = input('Введите строку: ').split()
max_len_word = ''
max_len = 0
for index in range(0, len(input_str)):
    if max_len < len(input_str[index]):
        max_len = len(input_str[index])
        max_len_word = input_str[index]

print(f'Самое длинное слово: {max_len_word}')
print(f'Длина этого слова: {max_len}')

# зачет!
