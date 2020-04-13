#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            grid[y][x] = '0'
            for next_move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + next_move[0], y + next_move[1]
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                    if grid[new_y][new_x] == '1':
                        dfs(new_x, new_y)
                        
        if not grid: return 0
        total = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == '1':
                    total += 1
                    dfs(x, y)
        return total
# @lc code=end
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
solution = Solution()
print(solution.numIslands(grid))
