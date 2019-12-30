#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Easy (20.88%)
# Likes:    405
# Dislikes: 577
# Total Accepted:    40K
# Total Submissions: 186.2K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\r\n[[],[1],[3],[1,2],[1],[1],[1]]\r'
#
# Design your implementation of the linked list. You can choose to use the
# singly linked list or the doubly linked list. A node in a singly linked list
# should have two attributes: val and next. val is the value of the current
# node, and next is a pointer/reference to the next node. If you want to use
# the doubly linked list, you will need one more attribute prev to indicate the
# previous node in the linked list. Assume all nodes in the linked list are
# 0-indexed.
#
# Implement these functions in your linked list class:
#
#
# get(index) : Get the value of the index-th node in the linked list. If the
# index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the
# linked list. After the insertion, the new node will be the first node of the
# linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked
# list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in
# the linked list. If index equals to the length of linked list, the node will
# be appended to the end of linked list. If index is greater than the length,
# the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the
# index is valid.
#
#
#
#
# Example:
#
#
# Input:
#
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
# Output:
# [null,null,null,null,2,null,3]
#
# Explanation:
# MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
#
#
#
# Constraints:
#
#
# 0 <= index,val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and
# deleteAtIndex.
#
#
#

# @lc code=start


class LinkedList(object):
    """Single linked list......

    Longer class information...

    Attributes:
        val: value
        next: next node
    """

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head is None or index >= self.size:
            return -1

        p = self.head
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            self.head = LinkedList(val)
            self.tail = self.head
        else:
            head = LinkedList(val)
            head.next = self.head
            self.head = head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = LinkedList(val)
            self.tail = self.head
        else:
            tail = LinkedList(val)
            self.tail.next = tail
            self.tail = tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return None
        if index == 0:
            self.addAtHead(val)
        else:
            insertnode = LinkedList(val)
            current = self.head
            for _ in range(index-1):
                current = current.next
            insertnode.next = current.next
            current.next = insertnode
            if insertnode.next is None:
                self.tail = insertnode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size or not self.head:
            return -1
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            p = self.head
            for _ in range(index-1):
                # consider when the index is at the end.
                if p.next is None:
                    return
                p = p.next
            p.next = p.next.next
            if p.next is None:
                self.tail = p
        self.size -= 1
# @lc code=end


my = MyLinkedList()
my.addAtHead(0)
my.addAtIndex(1, 1)
my.addAtTail(2)
my.addAtIndex(3, 3)
my.addAtTail(4)
my.deleteAtIndex(4)

