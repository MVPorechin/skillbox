decrypt_message = list(input('Сообщение: '))
swap = ''
encrypt_message = ''
for word in decrypt_message:
    if word.isalnum():
        swap = word + swap
    else:
        encrypt_message += swap
        encrypt_message += word
        swap = ''

print(f'Зашифрованное сообщение: {encrypt_message}')

# зачет!
