start_sequence = []
find_numbers_of_symmetry = []
finish_sequence = []
count_sequence = int(input('Кол-во чисел: '))
for _ in range(1, count_sequence + 1):
    number = int(input('Число: '))
    start_sequence.append(number)

print(f'Последовательность: {start_sequence}')

def symmetry(start_sequence):
    reverse_list = []
    for i_num in range(len(start_sequence) - 1, -1, -1):
        reverse_list.append(start_sequence[i_num])
    if start_sequence == reverse_list:
        return True
    else:
        return False
for i_nums in range(0, len(start_sequence)):
    for j_elem in range(i_nums, len(start_sequence)):
        finish_sequence.append(start_sequence[j_elem])
    if symmetry(finish_sequence):
        for i_check in range(0, i_nums):
            find_numbers_of_symmetry.append(start_sequence[i_check])
        find_numbers_of_symmetry.reverse()
        break
    finish_sequence = []

print(f'Нужно чисел: {len(find_numbers_of_symmetry)}\nCписок этих чисел: {find_numbers_of_symmetry}')

# зачет!
