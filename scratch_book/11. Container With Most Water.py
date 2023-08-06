#https://leetcode.com/problems/container-with-most-water/
#https://telegra.ph/13-Container-With-Most-Water-srednyaya-08-06
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        buy_price = height[0]
        for sell_price in height[1:]:
            buy_price = min(buy_price, sell_price)
            profit = sell_price - buy_price
            if profit > best_profit:
                best_profit = profit