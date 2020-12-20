#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        self.hashmap = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.hashmap:
            return self.hashmap[head]
        copy_node = Node(head.val)
        self.hashmap[head] = copy_node
        copy_node.next = self.copyRandomList(head.next)
        copy_node.random = self.copyRandomList(head.random)
        return self.hashmap[head]
# @lc code=end
