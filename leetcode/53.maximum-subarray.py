#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.77%)
# Likes:    5692
# Dislikes: 239
# Total Accepted:    708K
# Total Submissions: 1.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#

# @lc code=start

#%%
class Solution:
    def maxSubArray(self, nums) -> int:
        cur_max = glo_max = nums[0]
        for num in nums[1:]:
            cur_max = max(cur_max+num, num)
            glo_max = max(cur_max, glo_max)
        return glo_max

        

# @lc code=end
my = Solution()
print(my.maxSubArray([1]))
print(my.maxSubArray([-1]))

# %%
