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
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            v = letters[mid]
            if v <= target:
                left = mid + 1
            else:
                right = mid
        return letters[right % len(letters)]
# @lc code=end


my = Solution()
print(my.nextGreatestLetter(["c", "f", "j"], 'j'))
print(my.nextGreatestLetter(["c", "f", "j"], 'c'))
print(my.nextGreatestLetter(["c", "f", "j"], 'f'))
print(my.nextGreatestLetter(["c", "f", "j"], 'a'))
