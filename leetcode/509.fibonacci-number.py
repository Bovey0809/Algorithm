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
        # Dynamic 28ms
        left, right = 0, 1
        for _ in range(N):
            temp = left + right
            left, right = right, temp
        return left
# @lc code=end

me = Solution()
print(me.fib(4))