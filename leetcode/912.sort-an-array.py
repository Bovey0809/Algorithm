#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


import random


class Solution:
    def sortArray(self, nums):
        # quick sort
        def partition(nums, low, high):
            temp = nums[high]
            j = low - 1 
            for i in range(low, high):
                while nums[i] < temp:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
                
# @lc code=end


my = Solution()
test = [random.randint(1, 20) for _ in range(random.randint(0, 20))]
print(my.sortArray(test))
