guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def count_guests(guests):
    count = 0
    for _ in guests:
        count += 1
    return count

def main():
    message = ''
    while message != 'Пора спать':
        print(f'Сейчас на вечеринке {count_guests(guests)} человек: {guests}')
        message = input('Гость пришёл или ушёл?')
        if message == 'пришёл':
            name_guest = input('Имя гостя: ')
            if count_guests(guests) < 6:
                guests.append(name_guest)
                print(f'Привет, {name_guest}!\n')
            elif count_guests(guests) >= 6:
                print(f'Прости, {name_guest}, но мест нет.\n')
        elif message == 'ушёл':
            name_guest = input('Имя гостя: ')
            guests.remove(name_guest)
            print(f'Пока, {name_guest}\n')
    print('Вечеринка закончилась, все легли спать.')

main()

# зачет!
