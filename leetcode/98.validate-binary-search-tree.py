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
        def helper(root, low, high):
            if not root:
                return True
            if low < root.val < high:
                return helper(root.left, low, root.val) and helper(root.right, root.val, high)
            return False
        return helper(root, float('-inf'), float('inf'))


# @lc code=end
