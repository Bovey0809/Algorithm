#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start


class Solution:
    def coinChange(self, coins, amount) -> int:
        # dp function
        # minimum = min(amount, amount-coin + 1)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for remind in range(coin, amount + 1):
                dp[remind] = min(dp[remind], dp[remind-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
# @lc code=end