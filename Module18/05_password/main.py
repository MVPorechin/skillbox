count_lower_word = 0
count_upper_word = 0
count_number = 0
while True:
    password = input('Придумайте пароль: ')
    for word in password:
        if word.isupper():
            count_upper_word = 1
        elif word.islower():
            count_lower_word = 1
        elif word.isnumeric():
            count_number = 1
    if count_upper_word + count_lower_word + count_number < 3:
        count_lower_word = 0
        count_upper_word = 0
        count_number = 0
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

# зачет!
