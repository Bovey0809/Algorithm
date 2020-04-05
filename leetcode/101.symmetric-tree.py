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
        # using queue
        queue = [root, root]
        while queue:
            point1 = queue.pop(0)
            point2 = queue.pop(0)
            if point1 and point2:
                if point1.val != point2.val:
                    return False
                else:
                    queue.extend([point1.left, point2.right])
                    queue.extend([point1.right, point2.left])
            elif not point2 and not point1:
                continue
            else:
                return False
        return True
            

# @lc code=end
