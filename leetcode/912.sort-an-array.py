#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


import random


class Solution:
    def sortArray(self, nums):
        for i, num in enumerate(nums):
            j = i - 1
            while j >= 0 and nums[j] > num:
                nums[j+1] = nums[j]
                j -= 1
            nums[j + 1] = num
        return nums
# @lc code=end


my = Solution()
test = [random.randint(1, 10) for _ in range(random.randint(0, 10))]
print(my.sortArray(test))
