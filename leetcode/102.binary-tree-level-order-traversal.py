#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue


class Solution:
    def levelOrder(self, root):
        if not root:
            return
        level = [root]
        result = []
        while level:
            nodes = [node for node in level]
            result.append([node.val for node in nodes])
            pairs = [(node.left, node.right) for node in nodes]
            level = [node for pair in pairs for node in pair if node]
        return result
# @lc code=end


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

me = Solution()
print(me.levelOrder(root))
