from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = 0
        count_uniq = 1
        count_duplicate = 0
        for index in range(1, len(nums)):
            fast = nums[index]
            if slow == fast and count_uniq < 2:
                count_uniq += 1
            elif slow < fast or slow > fast:
                count_duplicate += count_uniq
                count_uniq = 1
                slow = nums[index]
                nums[count_duplicate] = nums[index]
        count_duplicate += count_uniq
        # nums[count_duplicate] = nums[-1]
        return count_duplicate, nums


my_sol = Solution()
print(my_sol.removeDuplicates(nums=[0,0,1,1,1,1,2,3,3]))
