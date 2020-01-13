# @lc app=leetcode id=532 lang=python3
# [532] K-diff Pairs in an Array

# @lc code=start
#%%
from collections import Counter
class Solution:
    def findPairs(self, nums, k: int) -> int:
        
        result = 0
        if k < 0:
            return result
        c = Counter(nums)
        if k == 0:
            for num in c:
                if c[num] > 1:
                    result += 1
            return result
        nums = set(nums)
        for item in nums:
            if item + k in nums:
                result += 1
        return result
        
# @lc code=end
my = Solution()
print(my.findPairs([1, 3, 1, 5, 4], 1))
print(my.findPairs([1, 2, 1, 3, 4], 0))

# %%
