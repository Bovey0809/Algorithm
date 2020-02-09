#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root) -> bool:
        # use recursion
        # base case
        def helper(root, minimum=float('-inf'), maximum=float('inf')):
            if not root:
                return True
            if minimum < root.val < maximum:
                return helper(root.left, minimum, root.val) and helper(root.right, root.val, maximum)
        return helper(root)
# @lc code=end
