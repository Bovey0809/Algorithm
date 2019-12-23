#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (45.21%)
# Likes:    751
# Dislikes: 126
# Total Accepted:    178.9K
# Total Submissions: 387.8K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a queue using stacks.
# 
# 
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# 
# 
# Example:
# 
# 
# MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
# 
# 
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
    
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1: self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2:
            return self.s2[-1]
        return self.front
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) + len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.peek()
obj.pop()
obj.empty()
