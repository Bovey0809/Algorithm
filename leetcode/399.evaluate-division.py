#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            g[a][b] = v
            g[b][a] = 1/v
            g[a][a] = 1
            g[b][b] = 1
        def dfs(start, destination, visited: set):
            if start not in g or destination not in g:
                return - 1.0
                
            stack = []
            stack.append((start, 1.0))
            
            while stack:
                cur, result = stack.pop()
                if cur == destination:
                    return result
                
                for c in g[cur]:
                    if c in visited:
                        continue
                    visited.add(c)
                    stack.append((c, result * g[cur][c]))
            return - 1
            
        return [dfs(start, destination, set()) for start, destination in queries]

# @lc code=end