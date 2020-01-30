#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# @lc code=start

class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
                continue
            if nums[mid] > target:
                right = mid - 1
                continue
        return -1
# @lc code=end

my = Solution()
print(my.search([-1, 0, 3, 5, 9, 12], 9))

