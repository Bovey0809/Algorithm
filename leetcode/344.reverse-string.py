
#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (64.23%)
# Likes:    970
# Dislikes: 598
# Total Accepted:    551K
# Total Submissions: 849.1K
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#
#
#
# Example 1:
#
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
#
#
# Example 2:
#
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
#
#

# @lc code=start


class Solution:

    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead, use recursion.
        """
        # base case
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                return helper(left + 1, right - 1)
        helper(0, len(s) - 1)

# @lc code=end
s = ["h", "e", "l", "l"]
Solution.reverseString(s)
print(s)
