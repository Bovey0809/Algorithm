#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (49.38%)
# Likes:    1208
# Dislikes: 1623
# Total Accepted:    349.6K
# Total Submissions: 703.2K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start
# %%
class Solution:
    def missingNumber(self, nums) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
# @lc code=end
my = Solution()
my.missingNumber([3, 0, 1])

# %%
