main_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

main_list.extend(second_list)
count_five = main_list.count(5)
for index in main_list:
    if index == 5:
        main_list.remove(index)
main_list.extend(third_list)
count_three = main_list.count(3)
print(f'Результат работы программы:\nКол-во цифр 5 при первом объединении: {count_five}')
print(f'Кол-во цифр 3 при первом объединении: {count_three}')
print(f'Итоговый список:  {main_list}')

# зачет!
