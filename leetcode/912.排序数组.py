#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low, high):
            temp = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] < temp:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        def quickSort(low, high):
            if low < high:
                pivot = partition(low, high)
                quickSort(low, pivot-1)
                quickSort(pivot+1, high)
        quickSort(0, len(nums) - 1)
        return nums
# @lc code=end
