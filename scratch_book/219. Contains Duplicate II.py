# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_dupl = dict()
        for index in range(len(nums)):
            if nums[index] in dict_dupl and abs(index - dict_dupl[nums[index]]) <= k:
                return True
            dict_dupl[nums[index]] = index
        return False


my_sol = Solution()
# my_sol.containsNearbyDuplicate(nums=[1,2,3,1], k=3)
print(my_sol.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
