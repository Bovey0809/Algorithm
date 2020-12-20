#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for res in range(coin, amount + 1):
                dp[res] = min(dp[res], dp[res - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else - 1                
# @lc code=end

