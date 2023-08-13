#56. Merge Intervals
# leetcode.com/problems/merge-intervals/description
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lst_one = intervals[0]
        lst_two = intervals[1]
        for lst in range(len(intervals)):
            print(intervals[lst])




my_sol = Solution
my_sol.merge(intervals=[[1,3],[2,6],[8,10],[15,18]])
print(my_sol)