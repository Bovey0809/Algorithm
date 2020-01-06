# @lc app=leetcode id=707 lang=python3
# @lc code=start


class node(object):
    """Double linked list......

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
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.size - 1:
            return -1
        if self.size == 1:
            return self.head.val
        p = self.head
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newhead = node(val)
        newhead.next = self.head
        self.head = newhead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newtail = node(val)
        if not self.head:
            self.head = newtail
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = newtail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return None
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        newnode = node(val)
        newnode.next = current.next
        current.next = newnode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.size - 1:  # 0 > 1 - 1
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            if current.next is None:
                current.next = None
            else:
                current.next = current.next.next
            self.size -= 1
# @lc code=end


my = MyLinkedList()
my.addAtHead(1)
print(my.get(0))
my.addAtTail(2)
my.addAtIndex(1, 2)
my.get(1)
my.deleteAtIndex(1)
my.get(1)
