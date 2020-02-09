#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums) -> int:
        write = 0
        for num in nums:
            if nums[write] != num:
                write += 1
                nums[write] = num
        return write + 1
# @lc code=end
