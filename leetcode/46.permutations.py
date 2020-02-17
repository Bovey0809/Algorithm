# @lc app=leetcode id=46 lang=python3
# @lc code=start


class Solution:
    def permute(self, nums: list) -> list:
        # recursion
        # base case
        result = []
        if len(nums) <= 1:
            return [nums]
        for index, num in enumerate(nums):
            for perm in self.permute(nums[:index] + nums[index + 1:]):
                result.append(perm + [num])
        return result
# @lc code=end


me = Solution()
print(me.permute([1, 2, 3]))
print(me.permute([1]))
