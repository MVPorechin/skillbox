nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [v_value for index, value in enumerate(nice_list) for i_index, i_value in enumerate(value) for v_index, v_value in enumerate(i_value)]

print(f'Результат: {result}')

# зачет!
