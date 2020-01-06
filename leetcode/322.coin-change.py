#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins, amount) -> int:
        def helper(coins, amount, cache):
            if amount <= 0 or amount < min(coins):
                return - 1
            minimum = amount
            # base case
            if amount in coins:
                cache[amount] = 1
                return 1
            elif amount in cache:
                return cache[amount]
            for coin in (c for c in coins if c <= amount):
                res = helper(coins, amount-coin, cache) + 1
                if res < amount:
                    minimum = res
                    cache[amount] = minimum
            return minimum
        output = helper(coins, amount, {})
        return output if output <= 0 else -1
# @lc code=end

me = Solution()
print(me.coinChange([2], 3))
print(me.coinChange([1, 2, 5], 11))

