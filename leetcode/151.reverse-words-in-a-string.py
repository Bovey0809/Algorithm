#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (18.1
# 
# 
# %)
# Likes:    733
# Dislikes: 2533
# Total Accepted:    334.8K
# Total Submissions: 1.8M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
# 
# 
# 
# Example 1:
# 
# 
# Input: "the sky is blue"
# Output: "blue is sky the"
# 
# 
# Example 2:
# 
# 
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
# 
# 
# Example 3:
# 
# 
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
# 
# 
# 
# 
# Note:
# 
# 
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
# 
# 
# 
# 
# Follow up:
# 
# For C programmers, try to solve it in-place in O(1) extra space.
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        """Find the word in an iteration and reverse it.
        
        Args:
            s: a sentence
        
        Returns:
            return the reversed sentence.
        """
        # find the word
        right = left = len(s) -1
        words = []
        while left >= 0:
            if s[left] != " ":
                right = left
                while left >= 0 and s[left] != " ":
                    left -= 1
                words.append(s[left+1:right+1])
            left -= 1
        return " ".join(words)
        
# @lc code=end
my = Solution()
print(my.reverseWords(" "))
print(my.reverseWords("the sky is blue"))
print(my.reverseWords("hello   world∞"))
