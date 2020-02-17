#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from queue import Queue


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = Queue()
        q.put(root)
        count, nextCount = 1, 0
        result = []
        level = []
        while not q.empty():
            node = q.get()
            count -= 1
            level.append(node.val)
            if node.left:
                q.put(node.left)
                nextCount += 1
            if node.right:
                q.put(node.right)
                nextCount += 1
            if count == 0:
                result.append(level)
                count, nextCount = nextCount, count
                level = []
        return result

# @lc code=end


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

me = Solution()
print(me.levelOrder(root))
