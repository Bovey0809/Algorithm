#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start

from bisect import bisect


class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        # binary search
        index = bisect(letters, target, 0, len(letters))
        return letters[index % len(letters)]
# @lc code=end


my = Solution()
print(my.nextGreatestLetter(["c", "f", "j"], 'j'))
print(my.nextGreatestLetter(["c", "f", "j"], 'c'))
print(my.nextGreatestLetter(["c", "f", "j"], 'f'))
print(my.nextGreatestLetter(["c", "f", "j"], 'a'))
