first_list = []
second_list = []
for num in range(1, 4):
    number = int(input(f'Введите {num}-е число для первого списка: '))
    first_list.append(number)
for num in range(1, 8):
    number = int(input(f'Введите {num}-е число для второго списка: '))
    second_list.append(number)

print(f'Первый список: {first_list}')
print(f'Второй список: {second_list}')

first_list.extend(second_list)
for value in first_list:
    for index in range(first_list.count(value) - 1):
        first_list.remove(value)
print(f'Новый первый список с уникальными элементами: {first_list}')

# зачет!
