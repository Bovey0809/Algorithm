#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a, b = 0, len(s) - 1
        while a < b:
            while a < b and not str.isalnum(s[a]):
                a += 1
            while a < b and not str.isalnum(s[b]):
                b -= 1
            if a < b and s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1
        return True
# @lc code=end


me = Solution()
me.isPalindrome("0P")
