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
        self.top = node(0)  # guard
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            return self.findCellBefore(index).next.val
        return -1            
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    
    def addAtIndex(self, index: int, val: int) -> None:
        newnode = node(val)
        afterMe = self.findCellBefore(index)
        newnode.next = afterMe.next
        afterMe.next = newnode
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            afterMe = self.findCellBefore(index)
            afterMe.next = afterMe.next.next
            self.size -= 1
        
    def findCellBefore(self, index):
        top = self.top
        count = 0
        while top.next:
            if count == index:
                return top # return the previous node.
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