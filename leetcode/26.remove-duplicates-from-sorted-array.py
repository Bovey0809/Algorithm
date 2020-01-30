#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        # use two pointers
        # use Python build in.
        if not nums: return 0
        
        read = write = 0
        while read < len(nums):
            while nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]
            read += 1
        return write + 1
# @lc code=end

