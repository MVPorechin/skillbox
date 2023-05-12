def compare(text):
    consonants = ['a', 'е', 'и', 'о', 'у', 'ы', 'э']
    output = []
    for i_text in text:
        for i_consonants in consonants:
            if i_consonants == i_text:
                output.append(i_text)
    return output


text = input('Введите текст: ')
print(f'Список гласных букв: {compare(text)}\nДлинна списка: {len(compare(text))}')

# зачет!
