# @lc app=leetcode id=225 lang=python3
# [225] Implement Stack using Queues
# @lc code=start
from queue import Queue
class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.size = 0
            
    def push(self, x: int) -> None:
        self.queue1.put(x)
        self.size += 1
        self.peak = x

    def pop(self) -> int:
        for _ in range(self.size - 1):
            x = self.queue1.get()
            self.peak = x
            self.queue2.put(x)
        x = self.queue1.get()
        self.queue1 = self.queue2
        self.size -= 1
        return x

    def top(self) -> int:
        return self.peak

    def empty(self) -> bool:
        return self.queue1.empty()
# @lc code=end


# %%
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.empty())
