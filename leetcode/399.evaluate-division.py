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
            g[b][a] = 1.0 / v
        def dfs(s, d):
            stack = [(s, 1.0)]
            seen = set()
            while stack:
                n, result = stack.pop()
                seen.add(n)
                for c in g[n]:
                    if c == d:
                        return result * g[n][c]
                    if not c in seen:
                        stack.append((c, result * g[n][c]))
            return - 1.0
        
        return [dfs(s, d) for s, d in queries]
# @lc code=end
me = Solution()
test_case = [[["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]], [3.0, 4.0, 5.0, 6.0], [["x2", "x2"]]]

print(me.calcEquation(*test_case))