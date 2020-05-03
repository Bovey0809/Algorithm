#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums) -> int:
        write = 0
        read = 0
        seen = set()
        while read < len(nums):
            if nums[read] not in seen:
                seen.add(nums[read])
                nums[write] = nums[read]
                write += 1
                read += 1
            else:
                read += 1
        return write
            
            
# @lc code=end
