#https://edu.tinkoff.ru/selection/76378fbd-1998-48fa-944e-eb736d321f11/exam/244?task=6
#https://telegra.ph/6-zadanie-07-11

def is_enough_a_pair(nums):
    incorrect_idxs = []
    for idx, val in enumerate(nums):
        if (idx + 1) % 2 != val % 2:
            incorrect_idxs.append(idx + 1)
        if len(incorrect_idxs) > 2:
            return -1, -1

    if len(incorrect_idxs) > 0:
        if len(incorrect_idxs) == 2 and incorrect_idxs[0] % 2 != incorrect_idxs[1] % 2:
            return incorrect_idxs
        return -1, -1

    if len(nums) > 2:
        return 1, 3
    return -1, -1


input()
nums = list(map(int, input().split()))

print(*is_enough_a_pair(nums))