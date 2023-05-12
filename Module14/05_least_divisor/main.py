def find_least_divisor(number):
    list_divisor = []
    for divisor in range(2, number + 1):
        if (number % divisor == 0):
            list_divisor.append(divisor)
    list_divisor.sort()
    return list_divisor[0]

number = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы: {find_least_divisor(number)}')


# зачет!
