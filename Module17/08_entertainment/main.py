import random
count_sticks = int(input('Введите кол-во палок: '))
count_stone_throws = int(input('Введите кол-во бросков камнем: '))
sticks = ['|' for index in range(count_sticks)]
count = 0
while count != count_stone_throws:
    left_index = random.randint(1, len(sticks))
    right_index = random.randint(1, len(sticks))
    if 1 <= left_index < right_index <= count_sticks:
        count += 1
        for index in range(1, len(sticks)):
            if left_index <= index < right_index:
                sticks[index] = '.'
        print(f'\nБросок {count}. Сбиты палки с номера {left_index + 1} по {right_index}')
        print(''.join(sticks))

# зачет!
