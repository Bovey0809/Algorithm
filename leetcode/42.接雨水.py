#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        size = len(height)
        ans = 0
        for i in range(1, size - 1):
            leftmax = max(height[: i + 1])
            rightmax = max(height[i:])
            ans += min(leftmax, rightmax) - height[i]
        return ans
# @lc code=end
