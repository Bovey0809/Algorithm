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
        """Two methods.
        
        1: inorder add root value, whethre sorted or not.(Logic bug: when one of a right tree node is equal to the root, failed.)
        
        2: recursive left and right tree.

        Args:
            root: a tree node
        
        Returns:
            return boolean
        """
        def maxnode(node):
            # base case
            if not node:
                return float('-inf')
            # recursive
            else:
                return max(node.val, maxnode(node.left), maxnode(node.right))
        def minnode(node):
            if not node:
                return float("inf")
            else:
                return min(node.val, minnode(node.left), minnode(node.right))
        # base case
        if not root: return True
        # recursive
        else:
            if maxnode(root.left) < root.val < minnode(root.right):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False
            

# @lc code=end

class TreeNode:
    """Tree Node for bianry tree.

    Attributes:
        val: value
        left: left node
        right: right node
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(5)
root.left = TreeNode(4)


me = Solution()
print(me.isValidBST(root))
