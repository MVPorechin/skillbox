from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        if len(prices) % 2 == 0:
            edge = len(prices) // 2
        else:
            edge = len(prices) // 2 + 1
        for buy_price in prices[:edge]:
            for sell_price in prices[edge:]:
                profit = sell_price - buy_price
                if profit > best_profit:
                    best_profit = profit

        return best_profit


my_sol = Solution()
result = my_sol.maxProfit(prices=[7,1,5,3,6,4])
print(result)
