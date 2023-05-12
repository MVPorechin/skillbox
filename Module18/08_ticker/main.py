def shift_list(list_string, shift):
    return list_string[shift:] + list_string[:shift]

def compare_list(first_list, second_list):
    for step in range(len(first_list)):
        if shift_list(second_list, step) == first_list:
            print(f'Первая строка получается из второй со сдвигом {step}')
        elif shift_list(second_list, step) != first_list and step == len(first_list):
            print(f'Первую строку нельзя получить из второй с помощью циклического сдвига.')


first_string = list(input('Первая строка: '))
second_string = list(input('Вторая строка: '))

compare_list(first_string, second_string)

# зачет!
