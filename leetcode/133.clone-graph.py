#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node):
        # Recusive Iteration
        if not node: return
        copy_node = Node(node.val)
        visited = {node: copy_node}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    copy_neighbor = Node(neighbor.val)
                    visited[neighbor] = copy_neighbor
                    visited[node].neighbors.append(copy_neighbor)
                    stack.append(neighbor)
                else:
                    visited[node].neighbors.append(visited[neighbor])
        return copy_node

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
