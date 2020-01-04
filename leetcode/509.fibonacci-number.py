#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        # Recursive 948ms
        # Iteration 28ms
        # Dynamic 
        left, right = 0, 1
        for i in range(N):
            left, right = right, left+right
        return left
# @lc code=end

me = Solution()
print(me.fib(0))

