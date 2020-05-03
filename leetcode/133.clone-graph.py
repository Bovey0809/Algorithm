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
        if not node:
            return None
        clone_graph = {node: Node(node.val)} # {node: clone_node}
        def dfs(node):
            for neighbor in node.neighbors:
                if neighbor in clone_graph:
                    clone_graph[node].neighbors.append(clone_graph[neighbor])
                else:
                    clone_neighbor = Node(neighbor.val)
                    clone_graph[neighbor] = clone_neighbor
                    clone_graph[node].neighbors.append(clone_neighbor)
                    dfs(neighbor)
                
        dfs(node)
        return clone_graph[node]

# @lc code=end
