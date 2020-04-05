#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_dict = {"(":")", "[":"]", "{":"}"}
        
        for p in s:
            if p not in pair_dict:
                if not stack:
                    return False
                else:
                    left = stack.pop()
                    if p != pair_dict[left]:
                        return False
            else:
                stack.append(p)
        if stack:
            return False
        return True

# @lc code=end
