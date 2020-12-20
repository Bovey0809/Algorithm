#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
# @lc code=end

