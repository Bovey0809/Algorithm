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
        if len(nums) == 1:
            return [nums]
        else:
            output = []
            for i, num in enumerate(nums):
                for perm in self.permute(nums[:i] + nums[i + 1 :]):
                    perm.append(num)
                    output.append(perm)   
        return output
# @lc code=end

me = Solution()
print(me.permute([1, 2, 3]))
print(me.permute([1]))

