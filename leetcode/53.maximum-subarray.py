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


class Solution:
    def maxSubArray(self, nums) -> int:
        # brute force O(n^2)
        length = len(nums)
        if length<=1:
            return nums[0]
        max_sum = nums[0]
        for index, num in enumerate(nums):
            for j in range(index, length):
                max_sum = max(max_sum, sum(nums[index: j+1]))
        return max_sum


# @lc code=end
my = Solution()
print(my.maxSubArray([-2, 1]))
