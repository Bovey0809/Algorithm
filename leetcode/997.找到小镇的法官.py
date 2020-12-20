#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#
from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        g = [0] * (N + 1)
        for a, b in trust:
            g[a] -= 1
            g[b] += 1
        return next(filter(lambda x: g[x] == N - 1, range(1, N + 1)), -1)

 # @lc code=end
