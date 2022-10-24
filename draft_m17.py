print('List comprehensions')
squares = [x ** 2 for x in range(10)]
print(f'{squares}\n')


def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)


prices_now = [1.9, 22.34, 56.3, 52.9, 88.5, 99.4]
first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))
prices_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
prices_second = [get_higher_price(second_percent, i_price)for i_price in prices_first]

print(f'Сумма цен за каждый год {round(sum(prices_now), 2), round(sum(prices_first), 2), round(sum(prices_second), 2)}')

print('17.1 - Задача 1. Кубы и квадраты')