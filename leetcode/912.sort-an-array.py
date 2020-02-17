#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


import random


class Solution:
    def sortArray(self, nums):
        def partition(nums, low, high):
            p = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] < p:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i + 1

        def quickSort(nums, low, high):
            if low < high:
                pivot = partition(nums, low, high)
                quickSort(nums, low, pivot - 1)
                quickSort(nums, pivot+1, high)
        quickSort(nums, 0, len(nums) - 1)
        return nums


# @lc code=end


my = Solution()
test = [random.randint(1, 10000) for _ in range(random.randint(0, 10))]
print(my.sortArray(test))
