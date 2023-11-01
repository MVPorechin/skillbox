class Solution(object):
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq_num = 0
        for index in range(len(nums)):
            if nums[index] not in nums[:index]:
                uniq_num += 1
                nums[uniq_num] = nums[index]
        return uniq_num, nums
        # left_point = 1
        # for right_point in range(1, len(nums)):
        #     if nums[right_point] != nums[right_point - 1]:
        #         nums[left_point] = nums[right_point]
        #         left_point += 1
        # return left_point


my_sol = Solution()
value = my_sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(value)
