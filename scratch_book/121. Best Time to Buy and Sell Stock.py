from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        left = len(prices) // 2
        for buy_price in range(left):
            for sell_price in range(len(prices)-1, left-1, -1):
                profit = prices[sell_price] - prices[buy_price]
                if profit > best_profit:
                    best_profit = profit

        return best_profit


my_sol = Solution()
result = my_sol.maxProfit(prices=[7,6,4,3,1])

print(result)