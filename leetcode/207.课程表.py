#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[a].append(b)
        colored = [0] * numCourses

        def dfs(c: int) -> bool:
            if colored[c] == -1:
                return False
            elif colored[c] == 1:
                return True
            colored[c] = -1
            for nei in g[c]:
                if not dfs(nei):
                    return False
            colored[c] = 1
            return True

        return all((dfs(c) for c in range(numCourses)))
# @lc code=end
