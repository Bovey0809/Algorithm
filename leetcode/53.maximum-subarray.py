# @lc app=leetcode id=53 lang=python3
# [53] Maximum Subarray
# @lc code=start


class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        cur_max = global_max = nums[0]
        for num in nums[1:]:
            cur_max = max(num, cur_max + num)
            global_max = max(global_max, cur_max)


# @lc code=end
my = Solution()
print(my.maxSubArray([1]))
print(my.maxSubArray([-1]))
print(my.maxSubArray([1, 2, 3]))
print(my.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# %%
