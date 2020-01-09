# @lc app=leetcode id=344 lang=python3
# @lc code=start
class Solution:        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def _reverse(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                _reverse(left+1, right-1)
        return _reverse(0, len(s)-1)
# @lc code=end

me = Solution()
s = ["h", "e", "l", "l", "o"]
me.reverseString(s)
print(s)
