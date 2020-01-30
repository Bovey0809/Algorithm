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
        q = Queue()
        q.put(root)
        count, next_count = 1, 0
        result = []
        nodes = []
        while not q.empty() and root:
            node = q.get()
            count -= 1
            nodes.append(node.val)
            if node.left:
                q.put(node.left)
                next_count += 1
            if node.right:
                q.put(node.right)
                next_count += 1
            if count == 0:
                result.append(nodes)
                nodes = []
                count, next_count = next_count, count
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
