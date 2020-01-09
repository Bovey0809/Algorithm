#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums:list) -> list:
        """Permutation using return unique result.
        
        Args:
            nums: list of integers.
        
        Returns:
            return list of ints.
        """
        # when num in nums is not unique, the output is the same.
        # base case: permutation one letter return itself.
        if len(nums) == 1:
            return [nums]
        output = []

        # recursion: permutate unique numbers.
        for num in set(nums):
            i = nums.index(num)
            for perm in self.permuteUnique(nums[:i] + nums[i + 1 :]):
                output.append([num] + perm)
        return output
# @lc code=end


me = Solution()
print(me.permuteUnique([1, 1, 2]))
