#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            g[a][b] = v
            g[b][a] = 1 / v

        def dfs(s, d, visited) -> int:
            if s not in g or d not in g:
                return - 1
            if s == d:
                return 1.0
            for nei in g[s]:
                if nei not in visited:
                    visited.add(nei)
                    temp = dfs(nei, d, visited)
                    if temp > 0:
                        return temp * g[s][nei]
            return - 1
    
        return [dfs(s, d, set()) for s, d in queries]


# @lc code=end
input = [[["x1", "x2"], ["x2", "x3"], ["x3", "x4"], [
    "x4", "x5"]], [3.0, 4.0, 5.0, 6.0], [["x1", "x5"]]]
me = Solution()
print(me.calcEquation(*input))
