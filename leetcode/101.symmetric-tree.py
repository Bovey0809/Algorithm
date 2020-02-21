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
        if not root:
            return True

        def helper(left, right):
            if left and right:
                if left.val == right.val:
                    return helper(left.left, right.right) and helper(left.right, right.left)
                else:
                    return False
            if (not left) and (not right):
                return True
            return False
        return helper(root.left, root.right)
# @lc code=end
