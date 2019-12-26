#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (53.80%)
# Likes:    978
# Dislikes: 124
# Total Accepted:    436.4K
# Total Submissions: 802.4K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
# %%
# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Detectect two strings are anagram.
        
        Args:
            s: one string.
            t: anthor string.
        
        Returns:
            return boolean.
        """
        c = Counter(s)
        for char in t:
            if char in c:
                c[char] -= 1
            else:
                return False
        for char in c:
            if c[char] != 0:
                return False
        return True

            
# @lc code=end