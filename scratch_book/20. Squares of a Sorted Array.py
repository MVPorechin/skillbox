from typing import List


#leetcode.com/problems/squares-of-a-sorted-array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        not_sort_list = []
        for n in nums:
            not_sort_list.append(pow(n, 2))

        print(not_sort_list,
              '\n',
              nums)


if __name__ == '__main__':
    my_sol = Solution()
    my_sol.sortedSquares(nums=[-4,-1,0,3,10])
