import re


example_list = ['9999999999', '999999-999', '99999x9999']
step_list = ['первый', 'второй', 'третий', 'четвертый', 'пятый', 'шестой', 'седьмой', 'восьмой', 'девятый']
file_pattern = r"\b[8-9]{10}"


if __name__ == "__main__":
    for text, position in zip(example_list, step_list):
        if re.findall(pattern=file_pattern, string=text):
            print(f'{position} номер: всё в порядке')
        else:
            print(f'{position} номер: не подходит')