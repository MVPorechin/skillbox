#56. Merge Intervals
# leetcode.com/problems/merge-intervals/description
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        out = [intervals[0]]
        for start, end in intervals[1:]:
            last = out[-1][1]
            if start <= last:
                out[-1][1] = max(last, end)
            else:
                out.append([start, end])
        return out


my_sol = Solution()
my_sol.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
print(my_sol)