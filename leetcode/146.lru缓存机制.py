#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class DoubleLinkedList:
    def __init__(self, val, key=0, prev=None, next=None):
        super().__init__()
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLinkedList(0)
        self.tail = DoubleLinkedList(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        key = self.tail.prev.key
        self.remove_node(self.tail.prev)
        return key

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        res = self.cache.get(key, -1)
        if res == -1:
            return res
        self.move_to_head(res)
        return res.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            node = DoubleLinkedList(value, key)
            self.cache[key] = node
            self.add_node(node)

        if len(self.cache) > self.capacity:
            key = self.remove_tail()
            del self.cache[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
