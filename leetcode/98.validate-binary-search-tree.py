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
        
        2: recursive left and right tree. (196ms slow)

        3: comapre root value with left and right. O(n)(44ms)

        4: change method 3 to iteration. O(n) (56ms)
            The iteration is a BFS, recursive is DFS, in BST, DFS seems faster.
        
        5. inorder traversal and judge.

        Args:
            root: a tree node
        
        Returns:
            return boolean
        """
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
            

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
