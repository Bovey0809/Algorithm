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
        """Inorder traversal iteration.
        
        Args:
            root: root of the tree.
        
        Returns:
            return list.
        """
        stack = []
        result = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()        
            result.append(root.val)
            root = root.right
        return result
# @lc code=end

class TreeNode(object):
    """Tree node
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

me = Solution()
me.inorderTraversal(root)


