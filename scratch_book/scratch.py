# def input_user_score():
#     count_records = int(input('Сколько записей вносится в протокол? '))
#     dict_records = dict()
#     print('Записи (результат и имя):')
#     for number in range(1, count_records + 1):
#         user_score = input(f'{number}-ая запись: ').split()
#         dict_records[number] = {}
#         dict_records[number]['name'] = user_score[1]
#         dict_records[number]['score'] = int(user_score[0])
#     return print(dict_records)


def result(records):
    list_records = [[record.get('score', 0), record.get('name', 0)] for index, record in records.items()]
    winner_rank = dict()
    max_value = max(list_records)
    winner_rank['First place'] = [max_value[1], max_value[0]]
    for index, values in records.items():
        if values.get('score') < max_value[0] and index < len(records.keys()):
            winner_rank['Second place'] = [values.get('name'), values.get('score')]
    for index, values in records.items():
        if values.get('score') <= winner_rank['Second place'][1] \
                and index < len(records.keys()) \
                and values.get('name') != winner_rank['Second place'][0]:
            winner_rank['Third place'] = [values.get('name'), values.get('score')]
    return winner_rank


def output_winner(list_rank):
    return [print(f'{index, value}') for index, value in list_rank.items()]

# dict_records = {
#     1: ('69485', 'Jack'),
#     2: ('95715', 'qwerty'),
#     3: ('95715', 'Alex'),
#     4: ('83647', 'M'),
#     5: ('197128', 'qwerty'),
#     6: ('95715', 'Jack'),
#     7: ('93289', 'Alex'),
#     8: ('95715', 'Alex'),
#     9: ('95715', 'M')
# }


dict_records = {
    1: {'name': 'Jack', 'score': 69485},
    2: {'name': 'qwerty', 'score': 95715},
    3: {'name': 'Alex', 'score': 95715},
    4: {'name': 'M', 'score': 83647},
    5: {'name': 'qwerty', 'score': 197128},
    6: {'name': 'Jack', 'score': 95715},
    7: {'name': 'Alex', 'score': 93289},
    8: {'name': 'Alex', 'score': 95715},
    9: {'name': 'M', 'score': 95715}
}


# user_score = input_user_score()
list_winner_rank = result(dict_records)
output_winner(list_winner_rank)




