# https://telegra.ph/5-zadanie-07-11

def increase_by_ten(step: int = 1, lenght: int = 1) -> int:
    """
    Функция создает шаг для счетчика
    на входе получаем количество разрядов создания шага
    на выходе число (шаг)
    :param step:
    :param lenght:
    :return:
    """
    if lenght == 1:
        return step
    else:
        lenght -= 1
        return increase_by_ten(step=step * 10 + 1, lenght=lenght)


def count(start: int, end: int, step: int) -> int:
    """
    Функция-счетчик через генератор
    на входе получаем границы старта, конца и шага,
    на выходе количество шагов
    """
    cnt = 0
    for _ in range(start, end, step):
        cnt += 1
    return cnt


def simple_or_not(left: int, right: int) -> int:
    """Для каждого разряда: 1-9, 10-99, 100-999 и тд. Всегда будем иметь только 9 подходящих нам чисел"""
    if len(str(right)) - len(str(left)) > 91:
        increase_first_step = increase_by_ten(lenght=len(str(left)))
        increase_second_step = increase_by_ten(lenght=len(str(right)))
        first_edge = 9 * increase_first_step
        second_edge = 9 * increase_second_step
        first_r = count(start=left, end=first_edge, step=increase_first_step)
        second_r = count(start=first_edge, end=right, step=increase_second_step)

        return first_r + second_r

    else:
        return count(start=left, end=right, step=increase_by_ten(lenght=len(str(left))))


l, r = map(int, input().split())
result = simple_or_not(left=l, right=r)
print(result)
