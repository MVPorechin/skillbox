#https://leetcode.com/problems/container-with-most-water/
#https://telegra.ph/13-Container-With-Most-Water-srednyaya-08-06
from typing import List


def min_value(first: int, second: int) -> int:
    """
    Моя функция для сравнения 2ух чисел и нахождения минимума среди их.
    :param first: первое целое число
    :param second: второе целое число
    :return int: минимальное число среди двух представленных
    """
    if first < second:
        return first

    return second


def max_value(first: int, second: int) -> int:
    """
    Моя функция для сравнения 2ух чисел и нахождения максимума среди их.
    :param first : Первое целое число
    :param second: второе целое число
    :return int: максимальное число среди двух представленных
    """
    if first > second:
        return first

    return second


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_sum = 0
        left = 0
        right = len(height) - 1

        if len(height) == 2 and height[left] == height[right]:
            max_sum = height[left]
        else:
            while left != right:
                gap = min_value(first=height[left], second=height[right]) * (right - 1)
                max_sum = max_value(first=max_sum, second=gap)

                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1

        return max_sum


my_sol = Solution()
res = my_sol.maxArea(height=[4,3,2,1,4])
print(res)
