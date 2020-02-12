# @lc app=leetcode id=151 lang=python3
# [151] Reverse Words in a String
# @lc code=start


class Solution:
    def reverseWords(self, s: str) -> str:
        pt = 0
        words = []
        while pt < len(s):
            if s[pt] != " ":
                start = pt
                while pt < len(s) and s[pt] != " ":
                    pt += 1
                word = s[start:pt]
                words.append(word)
            else:
                pt += 1
        return " ".join(list(reversed(words)))
# @lc code=end
