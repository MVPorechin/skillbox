def is_prime():
    return (number for number in range(2, 100) if all(number % num != 0 for num in range(2, number)))


def crypto(string):
    return [value for index, value in enumerate(list(string)) if index in is_prime()]


text = input('Введите текст: ')
print(crypto(text))

# зачет!
