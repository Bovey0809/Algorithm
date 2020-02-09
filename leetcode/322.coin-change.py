#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start


class Solution:
    def coinChange(self, coins, amount) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for change in range(coin, amount+1):
                dp[change] = min(dp[change], dp[change - coin] + 1)
        if dp[amount] == float('inf'):
            return - 1
        return dp[amount]
# @lc code=end


me = Solution()
print(me.coinChange([2], 3))
print(me.coinChange([1], 2))
print(me.coinChange([1, 2, 5], 11))
