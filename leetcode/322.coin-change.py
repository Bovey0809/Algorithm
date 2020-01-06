#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins, amount) -> int:
        def helper(coins, amount, cache):            
            # base case
            if amount == 0:
                return 0
            elif amount in cache:
                return cache[amount]
            # recursion
            cache[amount] = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    cache[amount] = min(helper(coins, amount - coin, cache) + 1, cache[amount])
            return cache[amount]
        answer = helper(coins, amount, {})
        return answer if answer != float('inf') else -1
            
# @lc code=end

me = Solution()
print(me.coinChange([2], 3))
print(me.coinChange([1], 2))
print(me.coinChange([1, 2, 5], 11))

