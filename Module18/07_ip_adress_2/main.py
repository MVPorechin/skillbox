def check_ip_correct_input(input_ip):
    for value in input_ip.split('.'):
        if value.find(',') == 1:
            return print('Адрес — это четыре числа, разделённые точками.')
        elif not value.isdigit():
            return print(f'{value} — это не целое число.')
        elif not 0 <= int(value) <= 255:
            return print(f'{value} превышает 255.')
    return print('IP-адрес корректен.')


input_str = input('Введите IP: ')

check_ip_correct_input(input_str)

# зачет!
