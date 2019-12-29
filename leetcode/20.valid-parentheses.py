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
        if len(s) % 2 != 0:
            return False
        opening = set('([{')
        match = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                # the paren is a closed one.
                if not stack:  # if stack is empty.
                    return False
                last_one = stack.pop()
                if match[last_one] != paren:
                    return False
        # if all the parentheses are opening.
        if stack: # stack is not empty
            return False
        return True
# @lc code=end
Solution().isValid("()")
Solution().isValid("((")
