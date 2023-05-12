count_friend = int(input('Кол-во друзей: '))
count_debt = int(input('Долговых расписок: '))

debt_base = []
for _ in range(1, count_friend + 1):
    friend = [_, 0]
    debt_base.append(friend)
for _ in range(1, count_debt + 1):
    print(f'{_}-я расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_many = int(input('Сколько: '))
    for index in debt_base:
        if index[0] == to_whom:
            index[1] -= how_many
        elif index[0] == from_whom:
            index[1] += how_many

print('Баланс друзей:\n')
for index in debt_base:
    print(f'Товарищ: {index[0]} Баланс: {index[1]}')

# зачет!
