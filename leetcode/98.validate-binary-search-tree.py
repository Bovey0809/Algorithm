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
        def _helper(root, minimum, maximum):
            # base case
            if not root:
                return True
            if minimum < root.val < maximum:
                return _helper(root.left, minimum, root.val) and _helper(root.right, root.val, maximum)
            return False
        return _helper(root, float('-inf'), float('inf'))

# @lc code=end
