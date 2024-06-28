from SecondLife import Karma

with open('karma.log', 'w', encoding='utf-8') as log_file:
    reincarnation = Karma(value=0)
    while reincarnation.get_karma() <= 500:
        try:
            output = reincarnation.one_day()
            if isinstance(output, tuple):
                karma_point, karma_except = output
                log_file.write(f'{str(type(karma_except)), str(karma_except)}''\n')
        finally:
            print(reincarnation)

