#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start

from bisect import bisect
class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        # use binary search
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            midvalue = letters[mid]
            if midvalue <= target:
                left = mid + 1
            if midvalue > target:
                right = mid
        return letters[right % len(letters)]
# @lc code=end


my = Solution()
print(my.nextGreatestLetter(["c", "f", "j"], 'j'), 'c')
print(my.nextGreatestLetter(["c", "f", "j"], 'c'), 'f')
print(my.nextGreatestLetter(["c", "f", "j"], 'f'), 'j')
print(my.nextGreatestLetter(["c", "f", "j"], 'a'), 'c')
