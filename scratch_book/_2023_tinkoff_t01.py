#
count_weapon, money = map(int, input().split())
price_weapon = list(map(int, input().split()))

# count_weapon = 5
# money = 13
# price_weapon = [3, 10, 300, 15,3]
best_buy = 0

for price in price_weapon:
    if money == price or (best_buy < price and money - price > 0):
        best_buy = price

print(best_buy)