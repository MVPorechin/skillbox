def main():
    select_menu = input('Выберите действие: 1 - Посмотреть текущий текст чата, 2 - Отправить сообщение: ')
    if select_menu == '1':
        return show_hystory_chat()
    elif select_menu == '2':
        input_username = input('Пожалуйста представьтесь: ')
        return telegram(input_username)
    else:
        print('Не распознал вашу команду, введите 1 или 2')
    return main()


def show_hystory_chat():
    try:
        with open('hystory.txt', 'r', encoding='utf-8') as hystory:
            [print(line) for line in hystory]
    except FileNotFoundError:
        print('История отсутствует')
    return main()


def telegram(username):
    with open('hystory.txt', 'a', encoding='utf-8') as hystory:
        message = input('Введите текст:')
        hystory.write(username + ': ' + str(message) + '\n')
    return main()


main()

# зачет!
