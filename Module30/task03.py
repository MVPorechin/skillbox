# map, filter
from typing import List

nums2: List[int] = [1, 2, 4, 5, 6, 7, 8, 54, 4, 52, 5, 6, 42, 62, 4, 56]
nums3: List[int] = [34, 3, 4, 23, 5, 1, 2, 1, 2, 5, 23, 4, 12, 3, 41, 23, 4, 12, 34]

result: List[map] = list(map(lambda x, y: x + y, nums2, nums3))
print(result)

print(list(map(lambda x, y: x + y, [1, 2], [1, 2, 3])))

result_even: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(result_even)

result = map(lambda num: num * 3, filter(lambda num: num % 2, nums2))
print(list(result))

result_2 = sum(map(lambda num: num * 3, filter(lambda num: num % 2, nums2)))
print(result_2)