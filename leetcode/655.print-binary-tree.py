#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def max_depth(root):
            if root:
                return 1 + max(max_depth(root.left), max_depth(root.right))
            else:
                return 0
        height = max_depth(root)

        level = collections.deque([root])
        output = []
        nodes = [] * (2 ** height)
        currenLevel = 1
        nextLevel = 0
        while level and root:
            node = level.popleft()
            nodes.append(node.val)
            currenLevel -= 1
            
            if node.left:
                level.append(node.left)
                nextLevel -= 1
            if node.right:
                level.append(node.right)
                nextLevel -= 1

            if not currenLevel:
                
                output.append(nodes)
                nodes = []
            
# @lc code=end

