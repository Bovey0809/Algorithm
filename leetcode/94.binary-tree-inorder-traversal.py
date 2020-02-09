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
        # Inoder traversal iteration using one stack.
        # The root value here is like a pointer.
        stack = []
        result = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:  # indicate the root is None and stack is not empty.
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
# @lc code=end
