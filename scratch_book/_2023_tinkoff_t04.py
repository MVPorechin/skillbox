# Похоже на разбор 4-ой, тут надо такую же табличку сделать, у нас это может быть словарь
# https://github.com/codedokode/pasta/blob/master/algorithm/atm.md
# def bank(n: int, a: list) -> bool:
#     a.sort()
#     minimum = 0
#     maximum = len(a) - 1
#     while minimum < maximum:
#         amount = a[minimum] + a[maximum]
#         if amount == n:
#             return True
#         elif amount < n:
#             minimum += 1
#         else:
#             maximum -= 1
#
#     return False

# n = int(input())
# a = list(map(int, input()))
# n, m = 5, 2
# a = [1, 2]

# решение 4-ой, но такое сабмитить нельзя, т.к. я его случайно засабмитил, чтобы проверить( Но можно чуть поменять,
# переставить

# from typing import Any
#
#
# def money_vault(nom_val: list, amount: int, count: int) -> Any:
#     sum_nominals = dict()
#     nominal_val_extend = nom_val * 2
#     # вот тут можно сделать по другому как минимум, это я массив х2 так сделал,
#     # можно попробовать в цикле.
#     for nominal_val in nominal_val_extend:
#         for s in list(sum_nominals.keys()):
#             if (s + nominal_val) not in sum_nominals:
#                 sum_nominals[s + nominal_val] = [nominal_val] + sum_nominals[s]
#         if nominal_val not in sum_nominals:
#             sum_nominals[nominal_val] = [nominal_val]
#
#     if amount in sum_nominals:
#         print(len(sum_nominals[amount]))
#         print(*sum_nominals[amount])
#     else:
#         print('-1')


# n, m = list(map(int, input().split()))
# nominal_value = list(map(int, input().split()))
n, m = 5, 2
nominal_value = [1, 2]
money_vault(nom_val=nominal_value, amount=n, count=m)

