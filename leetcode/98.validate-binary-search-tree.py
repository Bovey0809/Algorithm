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
        def _helper(node, minimum, maximum):
            if not node:
                return True
            if not minimum < node.val < maximum:
                return False
            return _helper(node.left, minimum, node.val) and _helper(node.right, node.val, maximum)
        return _helper(root, float('-inf'), float('inf'))
# @lc code=end
