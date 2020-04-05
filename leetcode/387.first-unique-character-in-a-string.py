# @lc app=leetcode id=387 lang=python3
# [387] First Unique Character in a String
# @lc code=start


from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for key in counter:
            if counter[key] == 1:
                return s.index(key)
        return -1
# @lc code=end

my = Solution()
print(my.firstUniqChar("leetcode"))
print(my.firstUniqChar("loveleetcode"))