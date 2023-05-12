goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
summ_quantity = 0
summ_price = 0
for g_key, g_value in goods.items():
    for s_key, s_value in store.items():
        if g_value == s_key:
            for index in s_value:
                for keys, values in index.items():
                    if keys == 'quantity':
                        summ_quantity += values
                        goods_value = values
                    if keys == 'price':
                        summ_price_per_goods = goods_value * values
                        summ_price += summ_price_per_goods

            print(f'{g_key} - {summ_quantity} штук(и), стоимость {summ_price} рубля(ей)')
            summ_quantity = 0
            summ_price = 0

# зачет!
