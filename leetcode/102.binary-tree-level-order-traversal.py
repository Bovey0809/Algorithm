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

import collections


class Solution:
    def levelOrder(self, root):
        level, output, nodes = collections.deque([root]), [], []
        current_count, next_count = 1, 0
        while level and root:
            node = level.popleft()
            current_count -= 1
            nodes.append(node.val)
            if node.left:
                level.append(node.left)
                next_count += 1

            if node.right:
                level.append(node.right)
                next_count += 1

            if not current_count:
                output.append(nodes)
                nodes = []
                current_count, next_count = next_count, current_count
        return output
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
