#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        def dfs(x, y):
            def valid(x, y):
                if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    return True
                else:
                    return False
                
            grid[y][x] = 0
            four_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for deltax, deltay in four_directions:
                new_x, new_y = x + deltax, y + deltay
                if valid(new_x, new_y):
                    if grid[new_y][new_x] == "1":
                        dfs(new_x, new_y)
                
                    
        count = 0
        
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == "1":
                    count += 1
                    dfs(x, y)
        return count
# @lc code=end
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
solution = Solution()
print(solution.numIslands(grid))
