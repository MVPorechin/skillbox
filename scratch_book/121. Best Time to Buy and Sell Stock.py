from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        buy_price = prices[0]
        for sell_price in prices[1:]:
            buy_price = min(buy_price, sell_price)
            profit = sell_price - buy_price
            if profit > best_profit:
                best_profit = profit

        return best_profit


my_sol = Solution()
result = my_sol.maxProfit(prices=[7,1,5,3,6,4])
print(result)
