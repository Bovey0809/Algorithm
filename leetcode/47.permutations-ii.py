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
        output = []
        for num in set(nums):
            index = nums.index(num)
            for perm in self.permuteUnique(nums[:index] + nums[index + 1 :]):
                output.append([num] + perm)
        return output
                
# @lc code=end


me = Solution()
print(me.permuteUnique([1, 1, 2]))
