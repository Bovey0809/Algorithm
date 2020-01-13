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
        
        5. inorder traversal and judge. O(n) (36ms)
            DFS using stack, inorder traversal iteration version.

        Args:
            root: a tree node
        
        Returns:
            return boolean
        """
        stack = []
        minimum = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= minimum:
                return False
            minimum = root.val
            root = root.right
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

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)


me = Solution()
print(me.isValidBST(root))
