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
        deque = [root]
        result = []
        levelcount = 1
        nextLevelCount = 0
        levelNodes = []
        while deque and root:
            root = deque.pop(0)
            levelcount -= 1
            levelNodes.append(root.val)
            if root.left:
                deque.append(root.left)
                nextLevelCount += 1
            if root.right:
                deque.append(root.right)
                nextLevelCount += 1
            if levelcount == 0:
                result.append(levelNodes)
                levelcount = nextLevelCount
                nextLevelCount = 0
                levelNodes = []
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
