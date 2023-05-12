import random


def lucky_number():
    with open('out_file.txt', 'w') as out_file:
        summ_number = 0
        chance_lst = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        try:
            while summ_number <= 777:
                input_number = int(input('Введите число: '))
                summ_number += input_number
                chance = random.choice(chance_lst)
                if chance:
                    raise Exception
                    break
                else:
                    out_file.write(str(summ_number) + '\n')
            print(f'Вы успешно выполнили условие для выхода из порочного цикла!')
        except (Exception,) as exc:
            print('Вас постигла неудача!')


lucky_number()

# зачет!
