#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# @lc code=end
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = a
b.next = c
c.next = d
d.next = b
print(Solution().hasCycle(a))
