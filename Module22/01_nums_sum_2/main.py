import os


def input_file(path):
    numbers_file = open(path, 'r')
    output_number_file = numbers_file.read()
    print(f'Содержимое файла numbers.txt\n{output_number_file}')
    numbers_file.close()

    count_values = [int(value) for value in open(path, 'r') if value not in [' ', '\n']]

    answer_file = open('answer.txt', 'w')
    answer_file.write(str(sum(count_values)))
    answer_file.close()

    return output_data(os.path.abspath(os.path.join('answer.txt')))


def output_data(path):
    answer_file_open = open(path, 'r')
    result_answer = answer_file_open.read()
    print(f'Содержимое файла {path}\n{result_answer}')
    answer_file_open.close()


path_to_file = os.path.abspath(os.path.join('numbers.txt'))
input_file(path_to_file)

# зачет!
