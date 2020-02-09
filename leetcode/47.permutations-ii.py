#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: list) -> list:
        result = []
        if len(nums) == 1:
            return [nums]
        for num in set(nums):
            index = nums.index(num)
            for perm in self.permuteUnique(nums[:index] + nums[index + 1 :]):
                result.append([num] + perm)
        return result
# @lc code=end


me = Solution()
print(me.permuteUnique([1, 1, 2]))
