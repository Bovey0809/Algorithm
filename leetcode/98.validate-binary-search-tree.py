#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root:TreeNode) -> bool:
        if not root:
            return True
        stack = []
        minimum = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= minimum:
                return False
            else:
                minimum = root.val
            root = root.right
        return True
# @lc code=end


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
my = Solution()
print(my.isValidBST(root))