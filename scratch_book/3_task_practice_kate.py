# У Кати насыщенный день на работе. Ей надо передать n разных договоров коллегам. Все встре- чи происходят на разных
# этажах, а между этажами можно перемещаться только по лестничным пролетам — считается, что это улучшает физическую
# форму сотрудников. Прохождение каждого пролета занимает ровно 11 минуту. Сейчас Катя на парковочном этаже,
# планирует свой маршрут. Коллег можно посетить в любом порядке, но один из них покинет офис через �t минут. С
# парковочного этажа лестницы нет — только лифт, на котором можно подняться на любой этаж. В итоге план Кати
# следующий: 1.	Подняться на лифте на произвольный этаж. Считается, что лифт поднимается на любой этаж за 00 минут.
# 2.	Передать всем коллегам договоры, перемещаясь между этажами по лестнице. Считается, что договоры на этаже
# передаются мгновенно. 3.	В первые �t минут передать договор тому коллеге, который планирует уйти. 4.	Пройти
# минимальное количество лестничных пролетов. Помогите Кате выполнить все пункты ее плана. Формат входных данных В
# первой строке вводятся целые положительные числа �n и �t (2≤�,�≤100)(2≤n,t≤100) — количество сотрудников и время,
# когда один из сотрудников покинет офис (в минутах). В следующей строке n чисел — номера этажей, на которых
# находятся сотрудники. Все числа различны и по абсолютной величине не превосходят 100. Номера этажей даны в порядке
# возрастания. В следующей строке записан номер сотрудника, который уйдет через t минут. Формат выходных данных
# Выведите одно число — минимально возможное число лестничных пролетов, которое понадобится пройти Кате. Замечание В
# первом примере времени достаточно, чтобы Катя поднялась по этажам по порядку. Во втором примере Кате понадобится
# подняться к уходящему сотруднику, а потом пройти всех остальных — например, в порядке {1,2,3,4,6}{1,2,3,4,6}
# 1 var
def clerk() -> int:
    count_spec, time = map(int, input().split())
    floors = list(map(int, input().split()))
    position_first = int(input())
    current_f = floors[position_first - 1]
    max_f = max(floors)
    min_f = min(floors)
    res = 0

    if current_f - min_f > time and (max_f - current_f) > time:
        res = min(current_f - min_f, max_f - current_f)

    res += max_f - min_f
    return res

# 2 var
count_spec, time = map(int, input().split())
floors = list(map(int, input().split()))
position_first = int(input())
min_max = floors[-1] - floors[0]
value = min(min_max + floors[-1] - floors[position_first - 1],
            min_max + floors[position_first - 1] - floors[0])
if time and sum(floors[:position_first - 1]) <= position_first:
    print(min_max)
else:
    print(value)



# def clerk() -> int:
#     count_spec, time = map(int, input().split())
#     floors = list(map(int, input().split()))
#     position_first = int(input())
#     min_max = floors[-1] - floors[0]
#     value = min(min_max + floors[-1] - floors[position_first - 1],
#                 min_max + floors[position_first - 1] - floors[0])
#     if time and sum(floors[:position_first - 1]) <= position_first:
#         return min_max
#     else:
#         return value
#
#
# print(clerk())


# count_spec, time = 6, 4
# floors = [1,  2,  3,  6,  8,  25]
# position_first = 5
# count_spec, time = 5, 5
# floors = [1,  4,  9,  16,  25]
# position_first = 2