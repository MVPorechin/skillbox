from TAX import Property, Apartment, Car, SummerHouse

wallet = int(input('Сколько у Вас денег?: '))
price_apartment = int(input('Сколько стоит квартира?: '))
price_car = int(input('Сколько стоит автомобиль?: '))
price_summer_house = int(input('Сколько стоит дача?: '))

summ_price = price_apartment + price_car + price_summer_house

my_apartment = Apartment(worth=price_apartment)
my_car = Car(worth=price_car)
my_summer_house = SummerHouse(worth=price_summer_house)

result_tax = my_apartment.set_tax() + my_car.set_tax() + my_summer_house.set_tax()
summ = summ_price + result_tax

print(f'Налог на квартиру составляет: {my_apartment.set_tax()}')
print(f'Налог на машину составляет: {my_car.set_tax()}')
print(f'Налог на дачу составляет:{my_summer_house.set_tax()}')
print(f'Итог: {summ}')
