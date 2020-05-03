# @lc app=leetcode id=53 lang=python3
# [53] Maximum Subarray
# @lc code=start


class Solution:
    def maxSubArray(self, nums) -> int:
        global_min = float('-inf')
        curmin = global_min
        for num in nums:
            curmin = max(num, curmin + num)
            global_min = max(curmin, global_min)
        return global_min

# @lc code=end
my = Solution()
print(my.maxSubArray([1]))
print(my.maxSubArray([-1]))
print(my.maxSubArray([1, 2, 3]))
print(my.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# %%
