#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, low, high):
            pivotvalue = nums[high]
            i = low - 1
            j = low
            while j < high:
                if nums[j] > pivotvalue:
                    j += 1
                else:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1

        def quicksort(nums, low, high):
            if low < high:
                pivot = partition(nums, low, high)
                quicksort(nums, low, pivot - 1)
                quicksort(nums, pivot + 1, high)
            return nums
        return quicksort(nums, 0, len(nums) - 1)
# @lc code=end
