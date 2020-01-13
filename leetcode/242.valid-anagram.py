# @lc app=leetcode id=242 lang=python3
# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        for char in t:
            if char in c:
                c[char] -= 1
            else:
                return False
        for char in c:
            if c[char] != 0:
                return False
        return True
# @lc code=end