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
        # Using stack, FILO
        # while push, detect whether it is a word.
        if len(s) < 1:
            return s
        
        length = len(s)
        words = []
        i = 0
        while i < length:
            if s[i] is not ' ':
                start = i
                while i < length and s[i] is not ' ':
                    i += 1
                words.append(s[start:i])
            i += 1
        
        # reverse
        last = len(words) - 1
        first = 0
        while last > first:
            words[last], words[first] = words[first], words[last]
            first += 1
            last -= 1
        
        # join
        word_length = len(words)
        if word_length == 0:
            return ""
            
        result = words[0]
        i = 1
        while i < word_length:
            result += ' '
            result += words[i]
            i += 1
        return result

# @lc code=end
my = Solution()
# my.reverseWords("the sky is blue")
print(my.reverseWords(" "))
