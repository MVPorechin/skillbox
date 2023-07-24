# n, k = map(int, input().split())
# numbers = list(map(int, input().split()))
n, k = 5, 2
numbers = [1, 2, 1, 3, 5]


def summary_value_in_list(lst: list) -> int:
    return sum(lst)


def increase(value: int) -> int:
    if 1 <= value < 9:
        return 9
    elif 10 <= value <= 99:
        return 90 + (value % 10)
    elif 100 <= value <= 999:
        return 900 + (value % 100)


def main(num: int, kom: int, list_num: list) -> int:
    first = summary_value_in_list(list_num)
    for index in range(num):
        if num == 1 and increase(value=list_num[index]) - list_num[index] == 0:
            return list_num
        # elif increase(value=list_num[index]) - list_num[index] >





        second = summary_value_in_list(numbers)
        return second - first


print(main(num=n, kom=k, list_num=numbers))
