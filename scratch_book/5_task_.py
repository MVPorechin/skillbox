from decimal import *


# https://telegra.ph/5-zadanie-07-11

def increase_by_ten(step: int = 1, lenght: int = 1) -> int:
    if lenght == 1:
        return step
    else:
        lenght -= 1
        return increase_by_ten(step=step * 10 + 1)


# def simple_or_not(first: int, second: int) -> int:
#     """для каждого разряда: 1-9, 10-99, 100-999 и тд. всегда будем иметь только 9 подходящих нам чисел"""
#     count = 0
#     if len(str(first)) != len(str(second)):
#         increase_first_step = increase_by_ten(lenght=len(str(first)))
#         increase_second_step = increase_by_ten(lenght=len(str(second)))
#     else:
#         increase_step = len(str(first))
#
#     step = increase_by_ten(lenght=increase_step)
#
#     for _ in range(first,second, step):
#         count += 1
#
#     return count
#
#
# result = simple_or_not(first=123, second=678)
step_ = increase_by_ten(lenght=3)
print(step_)
