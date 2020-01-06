#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
from functools import lru_cache
class Solution:
    @lru_cache
    def fib(self, N: int) -> int:
        # Recursive 948ms
        # Iteration 28ms
        # Dynamic 28ms
        if N == 0 or N == 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
# @lc code=end

me = Solution()
print(me.fib(0))

