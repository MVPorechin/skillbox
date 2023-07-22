# n, k = map(int, input().split())
# numbers = list(map(int, input().split()))
n, k = 5, 2
numbers = [1, 2, 1, 3, 5]

def summary_value_in_list(lst:list) -> int:
    return sum(lst)

def increase(value: int) -> int:
    if 1 <= value < 9:
        return 9
    elif 10 <= value <= 99:
        return 90 + (value % 10)
    elif 100 <= value <= 999:
        return 900 + (value % 100)

first = summary_value_in_list(numbers)

for index in range(len(numbers)):
    if summary_value_in_list(numbers[index]) - numbers[index]  :





second = summary_value_in_list(numbers)
print(second - first)
