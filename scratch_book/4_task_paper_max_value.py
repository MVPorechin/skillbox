# Задача 4 (2 вариант)
def foo(k, nums):
    num_count = {}
    for num in nums:
        for rank, n in enumerate(num[::-1]):
            if n == '9':
                continue
            key = 10 ** rank * (9 - int(n))
            num_count[key] = 1 + num_count.get(key, 0)

    val_count = sorted(num_count.items(), reverse=True)

    res = 0
    count_res = 0
    for val, count in val_count:
        for _ in range(count):
            res += val
            count_res += 1
            if count_res == k:
                return res
    return res


_, k = map(int, input().split())
nums = input().split()
print(foo(k, nums))