class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first = 0
        for second in range(len(nums)):
            if nums[second] != 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1

        return nums


my_solution = Solution()
print(my_solution.moveZeroes(nums=[1,0,0,1]))

