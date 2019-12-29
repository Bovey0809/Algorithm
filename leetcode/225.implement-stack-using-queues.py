#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (41.11%)
# Likes:    442
# Dislikes: 491
# Total Accepted:    152.4K
# Total Submissions: 363.2K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a stack using queues.
#
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
#
#
# Example:
#
#
# MyStack stack = new MyStack();
#
# stack.push(1);
# stack.push(2);
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
#
# Notes:
#
#
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
#
#
# @lc code=start
import collections
from collections import deque


class MyStack:
    """"Using queue to implement stack.

    In Python there is only deque, so that we only using
    popleft(), and append() methods.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        Methods could use:
            1. append
            2. popfromleft
        """
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        self.peak = x

    def pop(self) -> int:
        """Pop the ele from queue1 using popleft.

        Args:
            self.

        Returns:
            the poped item
        """
        length = len(self.queue1)
        for _ in range(length-1):
            self.peak = self.queue1.popleft()
        result = self.queue1.popleft()
        self.queue1 = self.queue2
        return result
        
    def top(self) -> int:
        """
        Get the top element.
        """
        
        return self.peak

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end


# %%
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.pop())
print(obj.top())
print(obj.empty())
