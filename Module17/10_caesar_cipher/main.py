def cipher(text, user_tab):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъьыэюя'
    temporary_text = ''
    word_list = [(alphabet[(alphabet.index(word) + user_tab) % 33] if word != ' ' else ' ') for word in text]
    for i_word in word_list:
        temporary_text += i_word
    return temporary_text


input_text = input('Скажи фразу: ')
tab = int(input('Введите сдвиг: '))

output_text = cipher(input_text, tab)

print(f'Зашифрованная строка: {output_text}')abet[(alphabet.index(word[letter]) + shift_word)]]