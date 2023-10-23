from typing import List

#leetcode.com/problems/squares-of-a-sorted-array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        sort_list = []
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                sort_list.append(nums[right] ** 2)
                right -= 1
            else:
                sort_list.append(nums[left] ** 2)
                left += 1
        return sort_list[::-1]


if __name__ == '__main__':
    my_sol = Solution()
    my_sol.sortedSquares(nums=[-4,-1,0,3,10])
