def number_backwards(number):
    reversed_number_string = str(number)[::-1]
    list_reversed_number_string = reversed_number_string.split('.')
    list_reversed_number_string.reverse()
    reversed_number = '.'.join(list_reversed_number_string)
    return reversed_number

def summ():
    summ = float(number_backwards(first_number)) + float(number_backwards(second_number))
    return summ

first_number = (input('Введите первое число: '))
second_number = (input('Введите второе число: '))


print(f'\nПервое число наоборот: {number_backwards(first_number)}')
print(f'Второе число наоборот: {number_backwards(second_number)}')
print(f'\nСумма: {summ()}')

# зачет!
