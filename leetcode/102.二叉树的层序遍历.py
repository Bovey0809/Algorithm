#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        result = []
        level = []
        count = 1
        nextlevel = 0
        while queue:
            node = queue.pop(0)
            count -= 1
            level.append(node.val)
            if node.left:
                queue.append(node.left)
                nextlevel += 1
            if node.right:
                queue.append(node.right)
                nextlevel += 1
            if count == 0:
                result.append(level)
                level = []
                count, nextlevel = nextlevel, count
        return result
            
# @lc code=end

