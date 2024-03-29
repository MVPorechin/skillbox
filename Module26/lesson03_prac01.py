# Задача 1. Бесконечный генератор По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой
# счётчик-генератор, который также в цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

def counter():
    count_value = 0
    while True:
        count_value += 1
        yield count_value


def get_prime_numbers(input_value):
    prime_numbers = []
    for number in range(2, input_value + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for i in get_prime_numbers(50):
    print(i, end='\t')
print()


# Задача 2. Очень большой файл Вам на обработку пришёл огромнейший файл с данными. Настолько огромный, что при его
# открытии компьютер просто зависает, так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не
# очень-то и «супер»).
#
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите программу,
# которая подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор.

def numbers_from_text(text):
    return [int(number) for number in text.rstrip().split()]


def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(numbers_from_text(line))
            yield clear_line_sum


all_sum = 0
for number in file_parser("numbers.txt"):
    all_sum += number

print("Вариант №1", all_sum)


# Ещё один вариант решения с функцией map()
def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(map(int, line.rstrip().split()))
            # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
            yield clear_line_sum


all_sum = 0
for number in file_parser("numbers.txt"):
    all_sum += number

print("Вариант №2", all_sum)