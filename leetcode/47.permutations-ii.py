#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: list) -> list:
        if len(nums) == 1:
            return [nums]
        result = []
        choose = set(nums)
        for num in choose:
            ind = nums.index(num)
            for perm in self.permuteUnique(nums[:ind] + nums[ind + 1 :]):
                perm.append(num)
                result.append(perm)
        return result
# @lc code=end


me = Solution()
print(me.permuteUnique([1, 1, 2]))
