def summary_number (number):
    summ = 0
    while number != 0:
        summ += number % 10
        number //= 10
        if number == 0:
            break
    return summ

def count_number (number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
        if number == 0:
            break
    return count

number = int(input('Введите число: '))
print(f' Сумма чисел: {summary_number(number)}')
print(f' Количество цифр в числе: {count_number(number)}')
print(f' Разность суммы и количества цифр: {abs(count_number(number)-summary_number(number))}')

# зачет!
