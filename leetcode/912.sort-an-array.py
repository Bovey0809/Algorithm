#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


import random


class Solution:
    def sortArray(self, nums):
        def merge(left, right):
            result = []
            while left and right:
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            if left:
                result += left
            if right:
                result += right
            return result
        
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        
        return mergeSort(nums)
# @lc code=end


my = Solution()
test = [random.randint(1, 20) for _ in range(random.randint(0, 20))]
print(my.sortArray(test))
