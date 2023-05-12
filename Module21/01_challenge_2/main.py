

def output_number(input_num):
    if input_num == 0:
        return input_num
    return output_number(input_num - 1), print(f'{input_num}')


input_number = int(input('Введите число: '))
output_number(input_number)

# зачет!
