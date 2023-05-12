with open('registrations.txt', 'r', encoding='utf-8') as reg_file,\
        open('registrations_good.log', 'w', encoding='utf-8') as reg_good_file, \
        open('registrations_bad.log', 'w', encoding='utf-8') as reg_bad_file:

    for line in reg_file:
        split_line = line.split()
        try:
            if len(split_line) > 2:
                if split_line[0].isalpha():
                    if split_line[1].find('@') > 1 and split_line[1].find('.') > 1:
                        if 9 < int(split_line[2]) < 100:
                            reg_good_file.write(str(line))
                        else:
                            # TODO смотрите, тут в круглых скобках можно передать текст ошибки ValueError("Мой кастомный текст данной ошибки")
                            raise ValueError('Поле «Имя» содержит НЕ только буквы')
                    else:
                        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
                else:
                    raise NameError('Поле «Возраст» НЕ является числом от 10 до 99')
            else:
                raise IndexError('НЕ присутствуют все три поля')
        # TODO теперь тут мы можем отловить все эти ошибки в скобках except (NameError, SyntaxError, ...) as e: и в переменной е будет текст ошибки, который вы указали выше, у каждой свой и его можно логгировать, то есть не надо будет делать столько однотипных строк
        except (NameError, SyntaxError, ValueError, IndexError) as exc:
            reg_bad_file.write(f'{str(line)[:-1]}\t\t\t\t{exc}\n')

# зачет!
