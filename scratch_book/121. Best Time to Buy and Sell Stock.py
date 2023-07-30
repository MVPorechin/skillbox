from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value, min_value = prices[-1], 1
        for index in range(len(prices), 0, -1):

            if prices[index - 1] > max_value:
                max_value = prices[index - 1]
            elif prices[index - 1] < max_value:
                min_value = prices[index - 1]
            # elif prices[index - 1] < max_value:
            #     prices[index - 1] = max_value

        max_value
        return max_value, min_value


my_sol = Solution()
result = my_sol.maxProfit(prices=[7,1,5,3,6,4])

print(result)