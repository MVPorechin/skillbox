shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_detail = input('Название детали:')
count_detail = 0
summary_price = 0
for index in shop:
        if index[0] == name_detail:
                count_detail += 1
                summary_price += index[1]

print(f'Кол-во деталей: {count_detail}')
print(f'Общая стоимость: {summary_price}')

# зачет!
