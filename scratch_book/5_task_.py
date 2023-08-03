from decimal import *
# https://telegra.ph/5-zadanie-07-11
def simple_or_not(first: int, second: int) -> int:
    """для каждого разряда: 1-9, 10-99, 100-999 и тд. всегда будем иметь только 9 подходящих нам чисел"""
    count = 0
    if first < 10:
        step = 1
    else:
        step = 10
    for _ in range(first, second, step):
        count += 1

    return count


result = simple_or_not(first=123, second=678)
print(result)