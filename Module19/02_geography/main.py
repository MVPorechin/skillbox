number_of_countries = int(input('Количество стран: '))
dict_country = dict()

for number_of_county in range(1, number_of_countries + 1):
    country = input(f'{number_of_county} страна: ').split()
    list_country = list(country)
    dict_country[list_country[0]] = list_country[1:]

count = 1
searching = True
while searching:
    check_city = False
    search_city = input(f'{count} город: ')
    for key, value in dict_country.items():
        if search_city in value:
            check_city = True
            print('Город', search_city, 'расположен в стране', key)

    if not check_city:
        searching = False
        print('По городу', search_city, 'данных нет')
    count += 1

# зачет!
