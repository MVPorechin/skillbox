input_str = input('Введите строку: ').split()
input_str_upper_lower = [word.capitalize() for word in input_str]

print('Результат:', ' '.join(input_str_upper_lower))

# зачет!
