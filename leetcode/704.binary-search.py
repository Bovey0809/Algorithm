#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# @lc code=start


class Solution:
    def search(self, nums, target: int) -> int:
        # reverse version Time Complexity Analyse
        def helper(nums, left, right):
            if left > right:
                return - 1
            mid = (ri
            ght - left) // 2 + left
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return helper(nums, mid+1, right)
            if nums[mid] > target:
                return helper(nums, left, mid - 1)
        return helper(nums, 0, len(nums))


# @lc code=end

my = Solution()
print(my.search([-1, 0, 3, 5, 9, 12], 9))
