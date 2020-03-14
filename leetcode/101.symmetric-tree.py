#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root, root]
        while q:
            a = q.pop(0)
            b = q.pop(0)
            if not a and not b:
                continue
            if a and b:
                if a.val == b.val:
                    q.extend([a.left, b.right, a.right, b.left])
                    continue
            return False
        return True
# @lc code=end
