#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.37%)
# Likes:    3795
# Dislikes: 190
# Total Accepted:    791.8K
# Total Submissions: 2.1M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        opening = set("({[")
        check = {'(': ')', '[': ']', '{': '}'}
        stack = []
        if len(s) % 2 != 0: return False
        for parenthese in s:
            if parenthese in opening:
                stack.append(parenthese)  
            else:
                if not stack:
                    return False
                last_opening = stack.pop()
                if parenthese != check[last_opening]:
                    return False
        if not stack:
            return True
        else:
            return False
        
# @lc code=end

Solution().isValid("()")
Solution().isValid("((")