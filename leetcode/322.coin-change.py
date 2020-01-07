#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins, amount) -> int:
        def helper(coins, amount, cache):
            if amount == 0:
                return 0
            if amount < 0:
                return - 1
            if amount in cache:
                return cache[amount]
            else:
                cache[amount] = float('inf')
            for coin in coins:
                if amount >= coin:
                    cache[amount] = min(cache[amount], helper(coins, amount - coin, cache) + 1)
            return cache[amount]
        result = helper(coins, amount, {})
        if result == float('inf'):
            return - 1
        else:
            return result
# @lc code=end

me = Solution()
print(me.coinChange([2], 3))
print(me.coinChange([1], 2))
print(me.coinChange([1, 2, 5], 11))

