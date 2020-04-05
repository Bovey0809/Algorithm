# @lc app=leetcode id=707 lang=python3
# @lc code=start


class node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.top = node(0)  # guard
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            return self.findCellBefore(index + 1).val
        return - 1
        
    def addAtHead(self, val: int) -> None:
        head = node(val)
        head.next = self.top.next
        self.top.next = head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        top = self.top
        while top.next:
            top = top.next
        top.next = node(val)
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            prev = self.findCellBefore(index)
            newnode = node(val)
            newnode.next = prev.next
            prev.next = newnode
            self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            prev = self.findCellBefore(index)
            prev.next = prev.next.next
            self.size -= 1

    def findCellBefore(self, index):
        top = self.top
        count = 0
        while top.next:
            if count == index:
                return top
            top = top.next
            count += 1
        return top
# @lc code=end


my = MyLinkedList()
my.addAtHead(1)
my.addAtTail(3)
my.addAtIndex(2, 2)
my.get(1)
my.deleteAtIndex(1)
my.get(1)
print(my)