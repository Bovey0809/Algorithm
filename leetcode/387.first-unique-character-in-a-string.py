#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.77%)
# Likes:    1324
# Dislikes: 92
# Total Accepted:    358.4K
# Total Submissions: 701.1K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#

# @lc code=start

import collections
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Find first unique char in a string.
        
        Args:
            s: a string.
        
        Returns:
            return the index of the first unique one.
        """
        c = Counter(s)
        for index, char in enumerate(s):
            if c[char] == 1:
                return index
        return  -1
                
        
# @lc code=end

my = Solution()
print(my.firstUniqChar("leetcodel"))
print(my.firstUniqChar("loveleetcode"))