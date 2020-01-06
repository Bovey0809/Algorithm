#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums) -> int:
        if len(nums) == 1:
            return [nums]
        output = []
        nums_set = set(nums)
        for num in nums_set:
            i = nums.index(num)
            for perm in self.permuteUnique(nums[:i]+nums[i+1:]):
                output.append(perm + [num])
        return output
# @lc code=end


me = Solution()
print(me.permuteUnique([1, 1, 2]))
