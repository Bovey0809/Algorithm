# @lc app=leetcode id=151 lang=python3
# [151] Reverse Words in a String
# @lc code=start


class Solution:
    def reverseWords(self, s: str) -> str:
        anchor = read = 0
        words = []
        while read < len(s):
            if s[read] != ' ':
                anchor = read
                while read < len(s) and s[read] != ' ':
                    read += 1
                word = s[anchor:read]
                words.append(word)
            else:
                read += 1
        return ' '.join(list(reversed(words)))
# @lc code=end


my = Solution()
print(my.reverseWords("the sky is blue"))
