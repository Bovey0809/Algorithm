#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


import random


class Solution:
    def sortArray(self, nums):
        # bubble sort
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
# @lc code=end


my = Solution()
test = [random.randint(1, 10000) for _ in range(random.randint(0, 10))]
print(my.sortArray(test))
