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
            for rem in range(coin, amount+1):
                dp[rem] = min(dp[rem], dp[rem - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
# @lc code=end

me = Solution()
print(me.coinChange([2], 3))
print(me.coinChange([1], 2))
print(me.coinChange([1, 2, 5], 11))

