#https://leetcode.com/problems/container-with-most-water/
#https://telegra.ph/13-Container-With-Most-Water-srednyaya-08-06
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_sum = 0
        left = 0
        right = len(height) - 1
        len_at_right = len(height)

        if len(height) == 2 and height[left] == height[right]:
            max_sum = height[left]
        else:
            while left != right:
                gap = min(height[left], height[right]) * (len_at_right -1)
                max_sum = max(max_sum, gap)

                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
                    len_at_right -= 1

        return max_sum


my_sol = Solution()
res = my_sol.maxArea(height=[4,3,2,1,4])
print(res)
