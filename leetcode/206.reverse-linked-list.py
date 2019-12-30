
# @lc app=leetcode id=206 lang=python3

# [206] Reverse Linked List

# https://leetcode.com/problems/reverse-linked-list/description/

# algorithms
# Easy (57.28%)
# Likes:    3246
# Dislikes: 77
# Total Accepted:    772.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]'

# Reverse a singly linked list.

# Example:


# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you
# implement both?



# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
      self.val = x
      self.next = None


class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        """reverse a link list in place.
        
        Args:
            head: the head node of the link list.
        
        Returns:
            return the head of the reversed link list.
        """
        current = head
        previous = None
        nextnode = None
        # Use one node to record the node previous.
        # Use the other two nodes to reverse.
        while current:
            """ Get the next node address first. And then reverse current and previous node. """
            nextnode = current.next # Get the next node first.
            current.next = previous
            previous = current
            current = nextnode
        return previous

# @lc code=end


