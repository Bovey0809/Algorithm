#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
from typing import List
# @lc code=start


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False

        colors = [-1] * len(graph)

        def dfs(node) -> bool:
            if colors[node] == -1:
                colors[node] = 1
            for nei in graph[node]:
                if colors[nei] != -1:
                    if colors[nei] == colors[node]:
                        return False
                else:
                    colors[nei] = colors[node] ^ 1
                    if not dfs(nei):
                        return False
            return True

        return all((dfs(i) for i in range(len(graph))))
# @lc code=end


me = Solution()
me.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
