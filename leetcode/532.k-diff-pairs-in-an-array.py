# @lc app=leetcode id=532 lang=python3
# [532] K-diff Pairs in an Array

# @lc code=start
from collections import Counter
class Solution:
    def findPairs(self, nums, k: int) -> int:
        if k < 0:
            return 0
        c = Counter(nums)
        count = 0
        for num in c:
            if k!=0 and num + k in c:
                count += 1
            elif k == 0 and c[num] > 1:
                count += 1
        return count
# @lc code=end
