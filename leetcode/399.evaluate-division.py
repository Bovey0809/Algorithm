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
        for (x, y), v in zip(equations, values):
            g[x][y] = v
            g[y][x] = 1 / v
        def dfs(src, dst):
            if not (src in g and dst in g):
                return - 1.0
            q, seen = [(src, 1.0)], set()
            for x, v in q:
                if x == dst:
                    return v
                seen.add(x)
                for y in g[x]:
                    if y not in seen:
                        q.append((y, v*g[x][y]))
            return - 1.0
        return [dfs(s, d) for s, d in queries]
        
# @lc code=end