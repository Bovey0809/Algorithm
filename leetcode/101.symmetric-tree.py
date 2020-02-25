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
        if not root:
            return True
        else:
            queue = [root.left, root.right]
            while queue:
                a = queue.pop(0)
                b = queue.pop(0)
                if a and b:
                    if a.val == b.val:
                        queue.extend([a.left, b.right, a.right, b.left])
                    else:
                        return False
                elif (not a) and (not b):
                    continue
                else:
                    return False
        return True
# @lc code=end
