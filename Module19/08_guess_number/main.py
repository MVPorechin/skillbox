import random
user_number = int(input('Введите максимальное число: '))
artem_number = random.randint(1, user_number)
guessed_number = True
while guessed_number:
    boris_speak = input('Нужное число есть среди вот этих чисел: ')
    if boris_speak != 'Помогите!':
        list_boris_speak = set(boris_speak)
        if str(artem_number) in list_boris_speak:
            print(f'Ответ Артёма: Да')
        else:
            print(f'Ответ Артёма: Нет')
    else:
        guessed_number = False
        print(f'Артём мог загадать следующие числа: {artem_number - 1, artem_number, artem_number + 1}')


# зачет!
