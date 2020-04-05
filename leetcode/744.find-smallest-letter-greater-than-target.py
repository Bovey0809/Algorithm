#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start

from bisect import bisect
class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        left, right = 0, len(letters)
        
        while left < right:
            middle = (left + right) // 2
            midvalue = letters[middle]
            if target == midvalue:
                left = middle + 1
            if target < midvalue:
                right = middle
            if target > midvalue:
                left = middle + 1        
        return letters[right % len(letters)]

# @lc code=end


my = Solution()
print(my.nextGreatestLetter(["c", "f", "j"], 'j'), 'c')
print(my.nextGreatestLetter(["c", "f", "j"], 'c'), 'f')
print(my.nextGreatestLetter(["c", "f", "j"], 'f'), 'j')
print(my.nextGreatestLetter(["c", "f", "j"], 'a'), 'c')
