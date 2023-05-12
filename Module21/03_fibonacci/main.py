def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


input_step_fibonacci = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {fibonacci(input_step_fibonacci)}')


# зачет!
