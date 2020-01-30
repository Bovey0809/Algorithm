#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        if not root: return
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

# @lc code=end

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)

me = Solution()
me.trimBST(root, 1, 2)