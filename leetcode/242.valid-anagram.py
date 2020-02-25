# @lc app=leetcode id=242 lang=python3
# @lc code=start

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# @lc code=end