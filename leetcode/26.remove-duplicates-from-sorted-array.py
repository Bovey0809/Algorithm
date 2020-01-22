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
        nums[:] = sorted(set(nums))
        return len(nums)
# @lc code=end

