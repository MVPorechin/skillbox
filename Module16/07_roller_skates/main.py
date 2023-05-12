list_roller_skate = []
list_people = []

count_roller_skate = int(input('Кол-во коньков: '))
for i_pair in range(1, count_roller_skate + 1):
    size = int(input(f'Размер {i_pair}-й пары: '))
    list_roller_skate.append(size)

count_people = int(input('\nКол-во людей: '))
for i_people in range(1, count_people + 1):
    size = int(input(f'Размер ноги {i_people}-го человека: '))
    list_people.append(size)

max_count_people = set(list_people) & set(list_roller_skate)
print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {len(max_count_people)}')

# зачет!
