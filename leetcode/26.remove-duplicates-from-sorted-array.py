#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums) -> int:
        write = 0
        for read in range(len(nums)):
            if read == len(nums) - 1 or nums[read] != nums[read + 1]:
                nums[write] = nums[read]
                write += 1
        return write
# @lc code=end
