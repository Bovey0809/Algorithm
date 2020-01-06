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
        # base case
        output = []
        if len(nums) == 1:
            return [nums]
        # recursion
        for i, num in enumerate(nums):
            for perm in self.permute(nums[:i] + nums[i + 1 :]): 
                perm.append(num)
                output.append(perm)
        [perm + num for i, num in enumerate(nums) for perm in self.permute(nums[:i]+nums[i+1:])]
        return output
# @lc code=end

me = Solution()
print(me.permute([1, 2, 3]))
print(me.permute([1]))

