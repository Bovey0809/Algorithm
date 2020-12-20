#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if left and right:
                if left.val == right.val:
                    return helper(left.left, right.right) and helper(left.right, right.left)
            return False
        if not root:
            return True
        return helper(root.left, root.right)

# @lc code=end
