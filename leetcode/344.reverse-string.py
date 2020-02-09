# @lc app=leetcode id=344 lang=python3
# @lc code=start


class Solution:
    def reverseString(self, s) -> None:
        def helper(s, left, right):
            if left <= right:
                s[left], s[right] = s[right], s[left]
                return helper(s, left + 1, right - 1)
        helper(s, 0, len(s) - 1)
# @lc code=end


me = Solution()
s = ["h", "e", "l", "l", "o"]
me.reverseString(s)
print(s)
