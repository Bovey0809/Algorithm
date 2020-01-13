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


from collections import deque
class Solution:
    def levelOrder(self, root):
        """Level order traversal.
        
        method1: Python List Comprehension
        method2: Using deque

        Args:
            root: treenode
        
        Returns:
            return level order.
        """
        level,  result = [root], []
        while level and root:
            result.append([node.val for node in level if node])
            pairs = [(node.left, node.right) for node in level if node]
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
