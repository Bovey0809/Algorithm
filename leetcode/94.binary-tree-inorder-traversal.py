#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        s = []
        result = []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            result.append(root.val)            
            root = root.right
        return result
# @lc code=end
