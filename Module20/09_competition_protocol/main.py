def input_user_score():
    count_records = int(input('Сколько записей вносится в протокол? '))
    winner = dict()
    first_place = [0, '']
    second_place = [0, '']
    third_place = [0, '']

    print('Записи (результат и имя):')
    for number in range(1, count_records + 1):
        user_score_list = input(f'{number}-ая запись: ').split()

        if first_place[0] < int(user_score_list[0]):
            third_place[0] = second_place[0]
            third_place[1] = second_place[1]
            winner['3'] = [third_place[0], third_place[1]]
            second_place[0] = first_place[0]
            second_place[1] = first_place[1]
            winner['2'] = [second_place[0], second_place[1]]
            first_place[0] = int(user_score_list[0])
            first_place[1] = user_score_list[1]
            winner['1'] = [first_place[0], first_place[1]]

        elif winner['2'][0] < int(user_score_list[0]) < winner['1'][0]:
            third_place[0] = second_place[0]
            third_place[1] = second_place[1]
            winner['3'] = [third_place[0], third_place[1]]
            second_place[0] = int(user_score_list[0])
            second_place[1] = user_score_list[1]
            winner['2'] = [second_place[0], second_place[1]]
            turn_third_place = True

        elif winner['2'][0] == int(user_score_list[0]) and winner['2'][1] != user_score_list[1]:
            if turn_third_place:
                winner['3'] = [int(user_score_list[0]), user_score_list[1]]
                turn_third_place = False

    return output_winner(winner)


def output_winner(list_rank):
    print(f'\nИтоги соревнований: ')
    return [print(f'{index}-е место. {value}') for index, value in sorted(list_rank.items())]


input_user_score()

# зачет!
