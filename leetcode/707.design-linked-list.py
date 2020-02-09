# @lc app=leetcode id=707 lang=python3
# @lc code=start


class node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        root = self.head
        if 0 <= index < self.size:
            for _ in range(index):
                root = root.next
            return root.val
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:
        newnode = node(val)
        if self.head:
            newnode.next, self.head = self.head, newnode
        else:
            self.head = newnode
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        root = self.head
        if not root:
            self.addAtHead(val)
        newnode = node(val)
        for _ in range(self.size - 1):
            root = root.next
        root.next = newnode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self.size:
            if index == 0: return self.addAtHead(val)
            if index == self.size: return self.addAtTail(val)
            
            root, newnode = self.head, node(val)
            for _ in range(0, index - 1):
                root = root.next
            newnode.next, root.next = root.next, newnode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            if index == 0:
                self.head = self.head.next
                self.size -= 1
                return
            root = self.head
            for _ in range(index - 1):
                root = root.next
            root.next = root.next.next
            self.size -= 1
# @lc code=end


my = MyLinkedList()
my.addAtHead(1)
my.addAtTail(3)
my.addAtIndex(1, 2)
my.get(1)
my.deleteAtIndex(1)
my.get(0)
