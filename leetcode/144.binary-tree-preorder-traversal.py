#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s = [root]
        result = []
        while s:
            root = s.pop()
            result.append(root.val)
            if root.right:
                s.append(root.right)
            if root.left:
                s.append(root.left)
        return result
# @lc code=end
