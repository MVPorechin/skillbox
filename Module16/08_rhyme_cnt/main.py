count_people = int(input('Кол-во человек: '))
number_out_people = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number_out_people}-й человек')
circle_people = list(range(1, count_people + 1))
index = 0

while len(circle_people) != 1:
    print(f'\nТекущий круг людей: {circle_people}')
    print(f'Начало счёта с номера: {circle_people[index]}')
    result = circle_people[(number_out_people + circle_people.index(circle_people[index]) - 1) % len(circle_people)]
    index = number_out_people % (len(circle_people) + 1)
    print(f'Выбывает человек под номером: {result}')
    circle_people.remove(result)
    if len(circle_people) <= 3:
        index = 0

print(f'\nОстался человек под номером: {circle_people[index]}')

# зачет!
