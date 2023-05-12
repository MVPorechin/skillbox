def add_contact(book):
    find_double = False
    name_surname = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
    for key in book.keys():
        if name_surname == key:
            find_double = True
    if find_double:
        return print('Такой человек уже есть в контактах')
    else:
        phone_number = int(input('Введите номер телефона: '))
        book[name_surname] = phone_number
        return book


def find_contact(book):
    search_by_name = input('Введите фамилию для поиска: ').title()
    return [
        print(' '.join(key_book), value_book)
        for key_book, value_book in book.items()
        if search_by_name in
           [
               key_book[0], key_book[0][:-1], key_book[1], key_book[1][:-1]]
    ]


def main():
    phone_book = dict()
    while True:
        answer = int(input('Введите номер действия:\n1. Добавить контакт\n2. Найти человека:\n'))
        if answer == 1:
            add_contact(phone_book)
            print(f'Текущий словарь контактов: {phone_book}')
        elif answer == 2:
            find_contact(phone_book)


main()

# зачет!
