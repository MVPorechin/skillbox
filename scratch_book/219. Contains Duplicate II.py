#https://leetcode.com/problems/contains-duplicate-ii/
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False


my_sol = Solution()
# my_sol.containsNearbyDuplicate(nums=[1,2,3,1], k=3)
print(my_sol.containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2))