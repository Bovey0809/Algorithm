# @lc app=leetcode id=344 lang=python3
# @lc code=start


class Solution:
    def reverseString(self, s) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                return helper(left+1, right-1)
        helper(0, len(s)-1)
        return s
# @lc code=end


me = Solution()
s = ["h", "e", "l", "l", "o"]
me.reverseString(s)
print(s)
