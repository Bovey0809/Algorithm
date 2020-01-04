# @lc app=leetcode id=46 lang=python3
# @lc code=start
class Solution:    
    def permute(self, nums:list) -> list:
        """Permuta distinct elements using RECURSION.
        
        Args:
            nums: list of int.
        
        Returns:
            return the permutation list of every possible.
        """
        output = []
        # base case
        if len(nums) == 1:
            return [nums]
        # recursion
        for i, let in enumerate(nums):
            for perm in self.permute(nums[:i] + nums[i+1:]):
                output += [perm + [let]]
        return output
# @lc code=end
