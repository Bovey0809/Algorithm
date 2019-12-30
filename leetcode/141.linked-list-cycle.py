#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (38.38%)
# Likes:    2080
# Dislikes: 307
# Total Accepted:    507K
# Total Submissions: 1.3M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        """Decide whehter there is a cycle.

        Using two pointers with different speed.

        Args:
            head: linked list

        Returns:
            return boolean value
        """
        # extreme case when head is None or head.next is None.
        slow = fast = head
        while fast and fast.next:
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
a.next = b
b.next = c
c.next = d
d.next = b
print(Solution().hasCycle(a))

a = ListNode(1)
print(Solution().hasCycle(a))


class LinkedList(object):
    """Single linked list.

    Linked list sample.

    Attributes:
        val: the value of the node.
        next: pointer to next link list node.
    """
    def __init__(self, val):
        self.val = val
        self.next = None

p = LinkedList('p')
a = LinkedList('a')
b = LinkedList('b')

p.next = a
a.next = b

print(p.val, p.next.val, p.next.next.val)

def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.next
        current.next = previous
        previous = current
        current = nextnode
    return previous

reverse(p)
