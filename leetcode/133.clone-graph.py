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
        def dfs(node, visited):
            copy_node = Node(node.val)
            visited[node]= copy_node
            for neighbor in node.neighbors:
                if neighbor in visited:
                    copy_node.neighbors.append(visited[neighbor])
                else:
                    copy_neighbor = Node(neighbor.val)
                    visited[neighbor] = copy_neighbor
                    copy_node.neighbors.append(dfs(neighbor, visited))
            return copy_node
        if not node:
            return None
        return dfs(node, {})
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
