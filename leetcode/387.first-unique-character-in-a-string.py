# @lc app=leetcode id=387 lang=python3
# [387] First Unique Character in a String
# @lc code=start

import collections
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)                
        for index, char in enumerate(s):
            if c[char] == 1:
                return index
        return -1
# @lc code=end

my = Solution()
print(my.firstUniqChar("leetcodel"))
print(my.firstUniqChar("loveleetcode"))