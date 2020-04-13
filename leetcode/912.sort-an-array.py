#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


import random


class Solution:
    def sortArray(self, nums):
        # insertion sort
        lengh = len(nums)
        for i in range(lengh):
            temp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > temp:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
        return nums
    
# @lc code=end


my = Solution()
test = [random.randint(1, 20) for _ in range(random.randint(0, 20))]
print(my.sortArray(test))
