from typing import List


class Solution:
    def removeDuplicates(self, nums):
        slow, fast = 0, 0
        while fast < len(nums):
            count = 1
            while fast + 1 < len(nums) and nums[fast] == nums[fast + 1]:
                fast += 1
                count += 1
            for index in range(min(2, count)):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

my_sol = Solution()
print(my_sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
