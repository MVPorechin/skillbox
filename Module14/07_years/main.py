def find_year():
    for year in range(start_year, end_year):
        thousand = (year // 1000) % 10
        hundred = (year % 1000) // 100
        dozen = (year % 1000) // 10 % 10
        units = year % 10
        if thousand == hundred == dozen or thousand == dozen == units or hundred == dozen == units:
            print(year)

start_year = int(input('Введите первый год: '))
end_year = int(input('Введите второй год: '))
print(f'Годы от {start_year} до {end_year} с тремя одинаковыми цифрами:')
find_year()

# зачет!
